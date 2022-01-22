from app import app
from flask import render_template
user = {"username":"Tayyar"}
@app.route('/')
@app.route('/page1')
def page1():
    return render_template("index.html",user=user)