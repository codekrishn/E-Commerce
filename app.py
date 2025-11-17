
from flask import Flask, render_template



app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/item_section')
def item_section():
    return render_template("item_section.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")



if __name__ == '__main__':
    app.run(debug=True)