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
    return render_template("addrecipe.html")

doc= {}

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    data = request.form.items()
    all_ingred = [];
    all_steps = [];
    for k, v in data: 
        if k.startswith('ing'):
            doc["recipe_ingredients"]=all_ingred
            all_ingred.append(v)
        elif k.startswith('step'):
            doc["recipe_steps"]=all_steps
            all_steps.append(v)
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