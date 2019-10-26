import os
from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')
app.config['SECRET_KEY'] = os.urandom(24)
mongo = PyMongo(app)

# Login / Registration page
@app.route('/')
def index():
    return render_template("index.html")

# Check data submitted via Registration form
@app.route('/register', methods=['POST'])
def register():
    users = mongo.db.users
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    registered = users.find_one({'username': username})
    if registered is None:
        users.insert_one({
            'username': username,
            'fullname': fullname,
            'password': password
        })
        success = True
        return render_template('index.html', success = success)
    success = False
    return render_template('index.html', success = success)

# Check data submitted via Login form
@app.route('/logout', methods=['POST'])
def login():
    users = mongo.db.users
    username = request.form.get('username')
    password = request.form.get('password')
    registered = users.find_one({'username': username, 'password': password})
    if registered is not None:
        session['username'] = username
        login = True
        return redirect(url_for('all_recipes'))
    login = False    
    return render_template('index.html', login=login)


# Redirects guest users to home page
@app.route('/guest_user')
def guest_user():
    return redirect(url_for('all_recipes'))

# Logout user by removing username from session
@app.route('/login')
def logout():
    session.clear()
    return render_template('index.html')

# Logout a user by removing username from session
@app.route('/all_recipes')
def all_recipes():
    recipes=mongo.db.recipes.find()
    cuisines =  mongo.db.cuisines.find()
    dishes=mongo.db.dishes.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    total_recipes=recipes.count()
    return render_template("home.html", recipes=recipes, dishes=dishes,
                            cuisines=cuisines, users=users, total_recipes=total_recipes, allergens=allergens)

# Home page displaying all recipes
@app.route('/the_recipe/<recipe_id>/<recipe_title>')
def the_recipe(recipe_id, recipe_title):
    recipes=mongo.db.recipes
    cuisines =  mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    return render_template("recipe.html",
                        recipe = recipes.find_one({'_id': ObjectId(recipe_id),'recipe_title': recipe_title}),
                        cuisines=cuisines, dishes=dishes, allergens=allergens, users=users)

# Display form to add a recipe
@app.route('/add_recipe')
def add_recipe():
    recipes=mongo.db.recipes.find()
    dishes=mongo.db.dishes.find()
    cuisines=mongo.db.cuisines.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    return render_template("addrecipe.html", cuisines=cuisines, dishes=dishes, 
                            recipes=recipes, allergens=allergens, users=users)

# Display form to edit the recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipes=mongo.db.recipes.find()
    dishes=mongo.db.dishes.find()
    cuisines=mongo.db.cuisines.find()
    allergens=mongo.db.allergens.find()
    users = mongo.db.users.find()
    return render_template('editrecipe.html',  
                        recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}),
                        cuisines = cuisines, dishes = dishes, allergens = allergens, users=users)

# Send form data to update recipe in DB
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe =  mongo.db.recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
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
        'recipe_steps':request.form.getlist('steps'),
    })
    return redirect(url_for('all_recipes'))

# Insert new recipe to DB collection
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    doc ={'recipe_author_name': session['username']}
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
    the_recipe=mongo.db.recipes
    the_recipe.insert_one(new_recipe)
    return redirect(url_for('all_recipes'))

# Removes a recipe from DB
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes')) 

# Search by Dish Types
@app.route('/search_dish/<dish_type>')
def search_dish(dish_type):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    dish_result = recipes.find({'dish_type': dish_type})
    dish_count = dish_result.count()
    return render_template('searchdish.html', result = dish_result, dish_type=dish_type,
                            count = dish_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens) 

# Search by Cuisine 
@app.route('/search_cuisine/<cuisine_name>')
def search_cuisine(cuisine_name):
    cuisines = mongo.db.cuisines.find()
    dishes = mongo.db.dishes.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    cuisine_result = recipes.find({'cuisine_name': cuisine_name})
    cuisine_count = cuisine_result.count()
    return render_template('searchcuisine.html', result = cuisine_result, cuisine_name = cuisine_name,
                            count = cuisine_count, cuisines=cuisines, dishes=dishes, users=users, allergens=allergens)

# Search by Allergens
@app.route('/search_allergen/<allergen_name>')
def search_allergen(allergen_name):
    dishes = mongo.db.dishes.find()
    cuisines = mongo.db.cuisines.find()
    users = mongo.db.users.find()
    allergens = mongo.db.allergens.find()
    recipes =  mongo.db.recipes
    allergen_result = recipes.find({'allergen_name':{'$not': {'$eq': allergen_name}}})
    allergen_count = allergen_result.count()
    return render_template('searchallergen.html', result = allergen_result, allergen_name=allergen_name, 
                            count = allergen_count, dishes=dishes, cuisines=cuisines, users=users, allergens=allergens)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)