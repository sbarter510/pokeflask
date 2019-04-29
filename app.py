from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_pymongo import PyMongo
from key import SECRET_KEY
import os

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'pokemon_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/pokemon_db'
app.config['SECRET_KEY'] = SECRET_KEY
db = PyMongo(app)




@app.route("/", methods = ["GET", "POST"])
def homepage():
    result = db.db.pokemon.find()
    return render_template("index.html", types = result)

@app.route('/results/name/<search>', methods = ["GET", "POST"] )

def search_results(search):
    name = search
    qry = db.db.pokemon.find({'name': name})
    return render_template('results.html', results=qry)

@app.route('/results/type/<typesearch>', methods = ["GET", "POST"] )

def type_results(typesearch):
    type_ = typesearch
    qry = db.db.pokemon.find({'type': type_ })
    return render_template('type.html', results=qry)

if __name__ == '__main__':
    app.run(debug=True)