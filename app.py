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
    return render_template("index.html",
    recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
    cuisines=mongo.db.cuisines.find(),
    dishes=mongo.db.dishes.find(),
    allergens=mongo.db.allergens.find())


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