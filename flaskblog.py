from flask import Flask, render_template,url_for,flash,redirect
from forms import registrationForm,loginForm
app = Flask(__name__)

app.config["SECRET_KEY"]="07b908b8c2903e92ab1202baa6069398"

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
	if form.validate_on_submit:
		flash(f'Account created for {form.username.data}!','Suceesss')
		return redirect(url_for('home'))
	return render_template("registration.html",title="Register",form=form)

@app.route('/login')
def login():
	form=loginForm()
	return render_template("login.html",title="Login",form=form)

if __name__=="__main__":
	app.run(debug=True)
