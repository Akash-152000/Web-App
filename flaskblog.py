from flask import Flask, render_template
app = Flask(__name__)

data=[{"First_name":"Akash","Second_name":"Yadav","Phone":"123456"},{"First_name":"Bhavna","Second_name":"Soni","Phone":"98765"}]


@app.route('/')
def hello_world():
    return render_template("home.html", data=data)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__=="__main__":
	app.run(debug=True)
