from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, AnyOf, URL, Optional, NumberRange 

class PetForm(FlaskForm):
     """Form for adding pets."""

     name = StringField("Pet Name",
                         validators=[InputRequired(message="name is Required! You can't leave it blank!")])
     
     species = StringField("Species",
                            validators=[AnyOf(["cat", "dog", "porcupine"], message="Choose from ")])
     
     photo_url = StringField("Photo URL",
                              validators=[URL(require_tld=True, message="Enter a valid URL address!"),
                                           Optional(strip_whitespace=True)])
     
     age = IntegerField("Age",
                         validators=[NumberRange(min=0, max=30, message="Age must be between 0 and 30!"),
                                      Optional(strip_whitespace=True)])
     
     notes = TextAreaField(
        "Comments",
        validators=[Optional()])

     available = BooleanField("Is Available", default="checked", false_values=(False, "false", ""))




class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL",
                              validators=[URL(require_tld=True, message="Enter a valid URL address!"),
                                           Optional(strip_whitespace=True)])

    notes = TextAreaField(
        "Comments",
        validators=[Optional()])

    available = BooleanField("Is Available")
