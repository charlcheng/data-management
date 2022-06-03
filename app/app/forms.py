from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm): 
    location = StringField("Search by Location", [DataRequired()])

    preference = SelectField(
        label = "preference", choices = [('museum','museum'),('milktea','milktea'),('bar','bar'),('restaurant','restaurant'),('theater','theater')]
    )
    submit = SubmitField("Search")
