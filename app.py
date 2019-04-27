from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_pymongo import PyMongo
from forms import pokeSearchForm
from key import SECRET_KEY

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'pokemon_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/pokemon_db'
app.config['SECRET_KEY'] = SECRET_KEY
db = PyMongo(app)




@app.route("/", methods = ["GET", "POST"])
def homepage():
    search = pokeSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    result = db.db.pokemon.find()
    return render_template("index.html", types = result, form=search)

@app.route('/results.html')

def search_results(search):

    results = []
    search_string = request.form['search']
    if search.data['search'] == '':
        qry = db.db.pokemon.find()
        results = qry
    if not results:
        flash('No results found!')

        return redirect('/')


    qry = db.db.pokemon.find({'name': search_string  })
    return render_template('results.html', results=qry)


if __name__ == '__main__':
    app.run(debug=True)