from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm, AccessDetailsForm, AccessProjectsForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd1b385daf2c84ddce08dd875c507e690'

posts = [
	{
		'author': 'XYZ',
		'title': 'Blog Post 1',
		'content': 'First Post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'ABC',
		'title': 'Blog Post 2',
		'content': 'Second Post content',
		'date_posted': 'April 21, 2018'
	}
]

projects = [
	{
		'author': 'XYZ',
		'title': 'Facial Recognition',
		'date_posted': 'January 30, 2020',
		'reference': 'https://arxiv.org/ftp/arxiv/papers/1302/1302.6379.pdf'
	},
	{
		'author': 'ABC',
		'title': 'E-learning',
		'date_posted': 'May 13, 2020',
		'link': 'https://files.eric.ed.gov/fulltext/EJ1062121.pdf'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'abcd@gmail.com' and form.password.data == 'abcd':
			flash('Login Successful!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password.', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/AccessDetails", methods=['GET', 'POST'])
def AccessDetails():
	form = AccessDetailsForm()
	if form.validate_on_submit():
		if form.email.data == 'abcd@gmail.com':
			return redirect(url_for('ShowDetails'))
		else:
			flash('Account does not exist. Please check email ID.', 'danger')
	return render_template('AccessDetails.html', title='Access Details', form=form)

@app.route("/ShowDetails")
def ShowDetails():
	return render_template('ShowDetails.html', title='Show Details')

@app.route("/AccessProjects", methods=['GET', 'POST'])
def AccessProjects():
	form = AccessProjectsForm()
	if form.validate_on_submit():
		if form.email.data == 'abcd@gmail.com':
			return redirect(url_for('ShowProjects'))
		else:
			flash('Account does not exist. Please check email ID.', 'danger')
	return render_template('AccessProjects.html', title='Access Projects', form=form)

@app.route("/ShowProjects")
def ShowProjects():
	return render_template('ShowProjects.html', title='Show Projects', projects=projects)

if __name__ == '__main__':
	app.run(debug=True)