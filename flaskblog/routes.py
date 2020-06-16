from flask import render_template,url_for,flash,redirect
from flaskblog.forms import registrationForm,loginForm
from flaskblog.models import User,Post
from flaskblog import app

data=[{"First_name":"Akash","Second_name":"Yadav","Phone":"123456","content":"COOL!!"},{"First_name":"Bhavna","Second_name":"Soni","Phone":"98765","content":"NICE!!"}]


@app.route('/')
def home():
    return render_template("home.html", data=data)

@app.route('/about')
def about():
    return render_template("about.html",title="TITLE")

@app.route('/register', methods=['GET','POST'])
def register():
	form=registrationForm()

	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','Suceesss')
		return redirect(url_for('home'))
	return render_template("registration.html",title="Register",form=form)

@app.route('/login',methods=['GET','POST'])
def login():
	form=loginForm()
	if form.validate_on_submit():
		if form.email.data=="admin@gmail.com" and form.password.data=="password":
			flash("Login success","success")
			return redirect(url_for("home"))
		else:
			flash("Login unsuccessful. Please check username and password","danger")
	return render_template("login.html",title="Login",form=form)