from flask import render_template,url_for,flash,redirect
from flaskblog.forms import registrationForm,loginForm
from flaskblog.models import User,Post
from flaskblog import app,db,bcrypt

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
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		user=User(username=form.username.data,email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to login','Suceesss')
		return redirect(url_for('login'))
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
