import os
from flask import Flask, render_template, redirect, url_for, request, session, Markup
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')
app.config['SECRET_KEY'] = '[R@ndom:-B]'
mongo = PyMongo(app)

success = Markup('<p>You are successfully registered. Please login below.</p>')
failure1 = Markup('<p>Sorry that username already exists</p>')
failure2 = Markup('<p>Login failed. Incorrect username or/and password.</p>')
Login = Markup('<i class="fas fa-sign-in-alt"></i> Login')
Logout = Markup('<i class="fas fa-sign-out-alt"></i> Logout')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    users = mongo.db.users
    registered = users.find_one({'username': username})
    if registered is None:
        users.insert_one({
            'username': username,
            'fullname': fullname,
            'password': password
        })
        return render_template('index.html', success = success)
    return render_template('index.html', failure1 = failure1)


@app.route('/logout', methods=['POST'])
def login():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    users = mongo.db.users
    registered = users.find_one({
        'username': username,
        'password': password
    })
    recipes=mongo.db.recipes.find()
    if registered is not None:
        session['username'] = username
        return render_template('home.html', user_status = Logout, recipes=recipes)
    return render_template('index.html', failure = failure2)

@app.route('/login')
def guest_user():
    recipes=mongo.db.recipes.find()
    return render_template('home.html', user_status = Login, recipes=recipes)

@app.route('/all_recipes')
def all_recipes():
    recipes=mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    cuisines=mongo.db.cuisines.find(),
    dishes=mongo.db.dishes.find(),
    allergens=mongo.db.allergens.find())

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('editrecipe.html',  
                        recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}),
                        cuisines = mongo.db.cuisines.find(),
                        dishes = mongo.db.dishes.find(),
                        allergens = mongo.db.allergens.find())
                        
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe =  mongo.db.recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
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


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    doc ={}
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

    recipe = doc
    recipes=mongo.db.recipes 
    recipes.insert_one(recipe)
    return redirect(url_for('all_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)