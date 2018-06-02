'''
This file contains all forms that will be needed for the 
gitfit website, including login form, registration form, 
etc. 

The flask wtforms module was used with gitfit to create
and handle all forms on the website
'''
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


'''
The below class defines the form for logging in to the website
This class inherits from the general flask form class
'''
class LoginForm(Form):
	# define error messages if validators do not pass
	bad_email = "Oops! You didn't enter an email address . . . "
	bad_password = "Oops! Your password must have a length between 8 and 80 characters . . . "
	# must define maximum and minimum accepted lengths for passwords
	MIN_PASSWORD_LENGTH = 8
	MAX_PASSWORD_LENGTH = 80
	# both variables below are the fields included in the log in page
	user = StringField('User Name', validators=[Email(message=bad_email), InputRequired()])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=MIN_PASSWORD_LENGTH, max=MAX_PASSWORD_LENGTH)])