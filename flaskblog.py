from flask import Flask, render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import registrationForm,loginForm
from datetime import datetime


app = Flask(__name__)
app.config["SECRET_KEY"]="07b908b8c2903e92ab1202baa6069398"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



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

if __name__=="__main__":
	app.run(debug=True)
