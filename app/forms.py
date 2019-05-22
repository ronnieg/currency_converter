from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, required


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CurrencyForm(FlaskForm):
    # currency = SelectField(choices=[('USD', 'EUR', 'BYN'), ('USD', 'EUR', 'BYN')])
    currency_from = SelectField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('BYN', 'BYN')])
    currency_to = SelectField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('BYN', 'BYN')])
    currency_count = IntegerField('Value', validators=[required()])
    submit = SubmitField('Confirm')