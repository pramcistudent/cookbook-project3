import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def all_recipes():
    recipes=mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


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
        'cuisine_name': request.form.getlist('cuisine_name'),
        'dish_type':request.form.getlist('dish_type'),
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
    insert_cuisine()
    insert_dish()
    return redirect(url_for('all_recipes'))

def insert_cuisine():
    doc2 ={}
    data = request.form.items()
    for k, v in data:
        if k == 'cuisine_name':
            doc2[k] = v
            cuisine = doc2
            cuisines=mongo.db.cuisines
            cuisines.insert_one(cuisine)

def insert_dish():
    doc3 ={}
    data = request.form.items()
    for k, v in data:
        if k == 'dish_type':
            doc3[k] = v
            dish = doc3
            dishes=mongo.db.dishes
            dishes.insert_one(dish)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)