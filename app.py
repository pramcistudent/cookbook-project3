import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/all_recipes')
def all_recipes():
    return render_template("index.html",
    dishes=mongo.db.dishes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
        port=int(os.environ.get('PORT')),
        debug=True)