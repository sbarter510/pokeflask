#from flask_wtf import Form
from wtforms import Form, StringField, SelectField

class pokeSearchForm(Form):

    choices = [('Name', 'Name'),

               ('Type', 'Type')]

    select = SelectField('Search for pokemon:', choices=choices)

    search = StringField('Enter Name or Type')