'''
The main handling page for gitfit website
uses flask to handle redirect for all different URL extensions
'''
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


# initialize the flask app, bootstrap, and the database
app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# must set a temporary secret key - this should be changed later 
# setting key this way is extremely unsecure
app.config['SECRET_KEY'] = 'Thisisnotevensecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/wolfecameron/Desktop/Projects/gitfit/database.db'


''' ----- TABLES FOR GITFIT DATABASE ----- '''
'''
this class creates the user table for the gitfit database
it inherits from the general SQLAlchemy model class
'''
class User(UserMixin, db.Model):
	# the user tables contains an id, username, email, and password
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True)
	email = db.Column(db.String(50), unique = True)
	password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

''' ----- MAIN HANDLER CODE FOR WEBSITE ----- '''

# handler for main page the redirects to login page
@app.route('/')
def home():
	return render_template('home.html')

# handler for login page 
@app.route('/login', methods=['GET','POST'])
def login():
	login_form = LoginForm()

	if login_form.validate_on_submit():
		# check to see if provided account exists within the database
		# you can get first result because usernames are unique
		user = User.query.filter_by(username=login_form.username.data).first()
		if user:
			# see if user's password matches what was entered
			if check_password_hash(user.password, login_form.password.data):
				login_user(user, remember=login_form.remember.data) # change to have a checkbox for remember later!
				return redirect('/user_dashboard')
			else:
				return "<h1>Log in failed.</h1>"
		else:
			return "<h1>Log in failed.</h1>" 

	return render_template('login.html', form = login_form)



# handler for the account creation page
@app.route('/register', methods=['GET','POST'])
def register():
	register_form = RegisterForm()

	if(register_form.validate_on_submit()):
		# add new user account into the existing database
		# hash password to an 80 character hashed password for security purposes
		hashed_password = generate_password_hash(register_form.password.data, method='sha256')
		newUser = User(username=register_form.username.data, email=register_form.email.data, password=hashed_password)
		db.session.add(newUser)
		db.session.commit()
		return "<h1>Your account has been created!</h1>"

	return render_template('register.html', form=register_form)

@app.route('/user_dashboard')
@login_required
def user_dashboard():
	return render_template('dashboard.html')

# run the app on local server if main file executed from terminal
if __name__ == '__main__':
	# run with debug == True so that issues can be seen
	app.run(debug=True)