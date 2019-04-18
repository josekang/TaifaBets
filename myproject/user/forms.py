from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from myproject.user.models import User


class LoginForm(FlaskForm):
    number = IntegerField("Phone Number: ", validators = [DataRequired("PLEASE ENSURE TO ENTER THE CORRECT INFORMATION")])
    password = PasswordField("Password: ", validators = [DataRequired("CHOOSE A STRONG PASSWORD")])
    submit = SubmitField("LOG IN") 


class RegisterForm(FlaskForm):
    username = StringField("Username: ", validators = [DataRequired("PLEASE ENSURE TO ENTER THE CORRECT INFORMATION")])
    number = IntegerField("Phone Number: ", validators = [DataRequired("PLEASE ENSURE TO ENTER THE CORRECT INFORMATION")])
    password = PasswordField("Password: ", validators = [DataRequired("CHOOSE A STRONG PASSWORD"), EqualTo("comfirm_password", message = "The passwords do not match")])
    comfirm_password = PasswordField("Comfirm Password", validators = [DataRequired("PLEASE ENSURE TO ENTER THE CORRECT INFORMATION")])
    submit = SubmitField("REGISTER")

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("The username has already been registered, please choose a different username")

    def check_number(self, field):
        if User.query.filter_by(number = field.data).first():
            raise ValidationError("The phone numberv has already been registered")
