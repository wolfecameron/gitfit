'''
The main handling page for gitfit website
uses flask to handle redirect for all different URL extensions
'''
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import LoginForm

app = Flask(__name__)
Bootstrap(app)

# must set a temporary secret key - this should be changed later 
# setting key this way is extremely unsecure
app.config['SECRET_KEY'] = 'Thisisnotevensecret'

# handler for main page the redirects to login page
@app.route('/')
def home():
	return render_template('home.html')

# handler for login page 
@app.route('/login', methods=['GET','POST'])
def login():
	login_form = LoginForm()
	if login_form.validate_on_submit():
		return "Information was submitted properly!"
	return render_template('login.html', form = login_form)

# run the app on local server if main file executed from terminal
if __name__ == '__main__':
	# run with debug == True so that issues can be seen
	app.run(debug=True)