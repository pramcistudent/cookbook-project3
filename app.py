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

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for("all_recipes"))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)