'''
This file contains all forms that will be needed for the 
gitfit website, including login form, registration form, 
etc. 

The flask wtforms module was used with gitfit to create
and handle all forms on the website
'''
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


'''
The below class defines the form for logging in to the website
This class inherits from the general flask form class
'''
class LoginForm(Form):
	# must define maximum and minimum accepted lengths for passwords
	MIN_PASSWORD_LENGTH = 8
	MAX_PASSWORD_LENGTH = 80
	MIN_USERNAME_LENGTH = 5
	MAX_USERNAME_LENGTH = 30
	# define error messages if validators do not pass
	bad_username = "Oops! Your username must have a length between {0} and {1} characters".format(str(MIN_USERNAME_LENGTH), str(MAX_USERNAME_LENGTH))
	bad_password = "Oops! Your password must have a length between {0} and {1} characters . . . ".format(str(MIN_PASSWORD_LENGTH), str(MAX_PASSWORD_LENGTH))
	# both variables below are the fields included in the log in page
	username = StringField('username', validators=[InputRequired(), Length(min=MIN_USERNAME_LENGTH, max=MAX_USERNAME_LENGTH, )])
	password = PasswordField('password', validators=[InputRequired(), Length(min=MIN_PASSWORD_LENGTH, max=MAX_PASSWORD_LENGTH, message = bad_password)])
	remember = BooleanField('Remember Me')

'''
The below class defines the form used for registering an account with gitfit
it inherits from the general flask forms class
'''
class RegisterForm(Form):
	# must define maximum and minimum accepted lengths for fields
	MIN_PASSWORD_LENGTH = 8
	MAX_PASSWORD_LENGTH = 80
	MIN_USERNAME_LENGTH = 5
	MAX_USERNAME_LENGTH = 30
	# define error messages if validators do not pass
	bad_email = "Oops! You didn't enter an email address . . . "
	bad_username = "Oops! Your username must have a length between {0} and {1} characters".format(str(MIN_USERNAME_LENGTH), str(MAX_USERNAME_LENGTH))
	bad_password = "Oops! Your password must have a length between {0} and {1} characters . . . ".format(str(MIN_PASSWORD_LENGTH), str(MAX_PASSWORD_LENGTH))
	# must define maximum and minimum accepted lengths for passwords
	# all variables below are properties of the registration form
	email = StringField('email', validators=[InputRequired(), Email(message=bad_email)])
	username = StringField('username', validators=[InputRequired(), Length(min=MIN_USERNAME_LENGTH, max=MAX_USERNAME_LENGTH, message = bad_username)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=MIN_PASSWORD_LENGTH, max=MAX_PASSWORD_LENGTH, message = bad_password)])
