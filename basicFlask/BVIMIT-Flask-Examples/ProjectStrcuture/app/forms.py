from flask_wtf import Form
from app import app
from wtforms import TextField
from wtforms.validators import Required

app.config['SECRET_KEY'] = 'Hard to guess string'
class NameForm(Form):
    name = TextField('What is your name?', validators = [Required()] )


