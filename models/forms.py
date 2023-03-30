from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class ContactForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    comment = CKEditorField('Comment: ', validators=[DataRequired()])
    submit = SubmitField('Submit comment')
