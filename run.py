import os
import math
from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')
app.config['SECRET_KEY'] = os.urandom(24)
mongo = PyMongo(app)

# DB Variables
users = mongo.db.users
recipes = mongo.db.recipes
cuisines = mongo.db.cuisines
dishes = mongo.db.dishes
allergens = mongo.db.allergens

# Login / Registration page
@app.route('/')
def index():
    return render_template("index.html")

# Sign in tab
@app.route('/signin')
def signin():
    signin = True
    return render_template("index.html", signin=signin)

# Sign up tab
@app.route('/signup')
def signup():
    signin = False
    return render_template("index.html", signin=signin) 


# Check data submitted via Registration form
@app.route('/register', methods=['POST'])
def register():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    registered = users.find_one({
        'username': {'$regex': username, '$options': 'i'}
    })
    if registered is None:
        users.insert_one({
            'username': username,
            'fullname': fullname,
            'password': password
        })
        success = True
        return render_template('index.html', success=success)
    success = False
    return render_template('index.html', success=success)

# Check data submitted via Login form
@app.route('/logout', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    registered = users.find_one({
        'username': {'$regex': username, '$options': 'i'}, 
        'password': password
    })
    if registered is not None:
        session['username'] = username
        login = True
        return redirect(url_for('all_recipes', num=1))
    login = False    
    return render_template('index.html', login=login)

# Redirects guest users to home page
@app.route('/guest_user')
def guest_user():
    return redirect(url_for('all_recipes', num=1))

# Logout user by removing username from session
@app.route('/login')
def logout():
    session.clear()
    return render_template('index.html')

# My recipes page
@app.route('/my_recipes/<username>/page:<num>')
def my_recipes(username, num):
    if username is not None:
        my_recipes = recipes.find({
            'recipe_author_name': {'$regex': username, '$options': 'i'}
        })
        total_my_recipes = my_recipes.count()
        
    total_pages = range(1, math.ceil(total_my_recipes/8) + 1)
    skip_num = 8 * (int(num) - 1)
    recipes_per_page = my_recipes.skip(skip_num).limit(8)
    
    if total_my_recipes <= 8:
        page_count = total_my_recipes
    elif (skip_num + 8) <= total_my_recipes:
        page_count = skip_num + 8
    else:
        page_count = total_my_recipes 
    return render_template("myrecipes.html", recipes=recipes.find(), dishes=dishes.find(), 
                    cuisines=cuisines.find(), allergens=allergens.find(), my_recipes=my_recipes, 
                    users=users.find(), total_pages=total_pages, num=num, skip_num=skip_num, 
                    page_count=page_count, total_my_recipes=total_my_recipes,
                    recipes_per_page=recipes_per_page)  

# Home page displaying all uploaded recipes
@app.route('/all_recipes/page:<num>')
def all_recipes(num):
    total_recipes=recipes.find().count()
    total_pages = range(1, math.ceil(total_recipes/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = recipes.find().skip(skip_num).limit(8)
    
    if total_recipes <= 8:
        page_count = total_recipes
    elif (skip_num + 8) <= total_recipes:
        page_count = skip_num + 8
    else:
        page_count = total_recipes
    return render_template("home.html", recipes=recipes.find(),
            dishes=dishes.find(), cuisines=cuisines.find(), users=users.find(), 
            allergens=allergens.find(), total_pages=total_pages, skip_num=skip_num, 
            num=num, page_count=page_count, recipes_per_page=recipes_per_page, 
            total_recipes=total_recipes)
    
# Displays detail view of a recipe
@app.route('/the_recipe/<recipe_id>/<recipe_title>')
def the_recipe(recipe_id, recipe_title):
    return render_template("recipe.html", cuisines=cuisines.find(),  
            allergens=allergens.find(), users=users.find(), dishes=dishes.find(),
            recipe=recipes.find_one({'_id': ObjectId(recipe_id),
            'recipe_title': recipe_title}))

# Display form to add a recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", cuisines=cuisines.find(), 
            dishes=dishes.find(), recipes=recipes.find(), users=users.find(), 
            allergens=allergens.find())

# Display form to edit the recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('editrecipe.html', cuisines=cuisines.find(), 
            dishes=dishes.find(), allergens=allergens.find(), users=users.find(),
            recipe=recipes.find_one({"_id": ObjectId(recipe_id)}))

# Send form data to update recipe in DB
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes.update( {'_id': ObjectId(recipe_id)},
    { 
            '$set':{
                'recipe_author_name': session['username'],
                'recipe_title':request.form.get('recipe_title'),
                'recipe_short_description':request.form.get('recipe_short_description'),
                'recipe_image_url': request.form.get('recipe_image_url'),
                'cuisine_name': request.form.get('cuisine_name'),
                'dish_type':request.form.get('dish_type'),
                'allergen_name':request.form.getlist('allergen_name'),
                'recipe_prep_time':request.form.get('recipe_prep_time'),
                'recipe_cook_time':request.form.get('recipe_cook_time'),
                'total_time':request.form.get('total_time'),
                'recipe_serves':request.form.get('recipe_serves'),
                'recipe_ingredients':request.form.getlist('ingred'),
                'recipe_steps':request.form.getlist('steps')
            }
        })
    return redirect(url_for('my_recipes', username=session['username'], num=1))

# Insert new recipe to DB collection
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    doc = {'recipe_author_name': session['username']}
    data = request.form.items()
    all_ingred = request.form.getlist('ingred')
    all_steps = request.form.getlist('steps')
    all_allergens = request.form.getlist("allergen_name")
   
    for k, v in data: 
        if k == "ingred":
            doc["recipe_ingredients"]=all_ingred
        elif k == "steps":
            doc["recipe_steps"]=all_steps
        elif k == "allergen_name":
            doc["allergen_name"] = all_allergens
        else:
            doc[k]= v  

    new_recipe = doc
    recipes.insert_one(new_recipe)
    return redirect(url_for('my_recipes', username=session['username'], num=1))

# Removes a recipe from DB
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipes', username= session['username'], num=1)) 

# Search by Dish Types
@app.route('/search_dish/<dish_type>/page:<num>')
def search_dish(dish_type, num):
    dish_result = recipes.find({'dish_type': dish_type})
    dish_count = dish_result.count()
    total_pages = range(1, math.ceil(dish_count/8) + 1)
    skip_num = 8 * (int(num) - 1)
    recipes_per_page = dish_result.skip(skip_num).limit(8)
    if dish_count <= 8:
        page_count = dish_count
    elif (skip_num + 8) <= dish_count:
        page_count = skip_num + 8
    else:
        page_count = dish_count
    return render_template('searchdish.html', dish_type=dish_type, num=num, 
            total_pages=total_pages, page_count=page_count, skip_num=skip_num, 
            recipes_per_page=recipes_per_page, count=dish_count, dishes=dishes.find(), 
            cuisines=cuisines.find(), users=users.find(), allergens=allergens.find())  

# Search by Cuisine 
@app.route('/search_cuisine/<cuisine_name>/page:<num>')
def search_cuisine(cuisine_name, num):
    cuisine_result = recipes.find({'cuisine_name': cuisine_name})
    cuisine_count = cuisine_result.count()
    total_pages = range(1, math.ceil(cuisine_count/8) + 1)
    skip_num = 8 * (int(num) - 1)
    recipes_per_page = cuisine_result.skip(skip_num).limit(8)
    
    if cuisine_count <= 8:
        page_count = cuisine_count
    elif (skip_num + 8) <= cuisine_count:
        page_count = skip_num + 8
    else:
        page_count = cuisine_count 
    return render_template('searchcuisine.html', recipes_per_page=recipes_per_page, 
            num=num, cuisine_name=cuisine_name,  skip_num=skip_num, total_pages=total_pages, 
            page_count=page_count, count=cuisine_count, cuisines=cuisines.find(), 
            dishes=dishes.find(), users=users.find(), allergens=allergens.find())

# Search by Allergens
@app.route('/search_allergen/<allergen_name>/page:<num>')
def search_allergen(allergen_name, num):
    allergen_result = recipes.find({'allergen_name':
        {'$not': {'$eq': allergen_name}}})
    allergen_count = allergen_result.count()
    total_pages = range(1, math.ceil(allergen_count/8) + 1)
    skip_num = 8 * (int(num)-1)
    recipes_per_page = allergen_result.skip(skip_num).limit(8)
    
    if allergen_count <= 8:
        page_count = allergen_count
    elif (skip_num + 8) <= allergen_count:
        page_count = skip_num + 8
    else:
        page_count = allergen_count
    return render_template('searchallergen.html', num=num, allergen_name=allergen_name, 
            total_pages = total_pages, skip_num=skip_num, page_count=page_count, 
            recipes_per_page=recipes_per_page, count=allergen_count, dishes=dishes.find(), 
            cuisines=cuisines.find(), users=users.find(), allergens=allergens.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=False)