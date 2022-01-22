from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    # return "Hello World!"
    user = {"kullaniciadi":"Bugra"}
    return render_template("index.html",title="",)