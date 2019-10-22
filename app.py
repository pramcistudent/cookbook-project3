import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/all_recipes')
def all_recipes():
    return render_template("allrecipes.html",
    dishes=mongo.db.dishes.find())
    
@app.route('/recipe_form')
def recipe_form():
    return render_template("addrecipe.html",
    allergens=mongo.db.allergens.find(),
    cuisines=mongo.db.cuisines.find(),
    dishes=mongo.db.dishes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)