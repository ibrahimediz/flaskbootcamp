from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {"kullaniciadi":"Furkan"}
    return render_template("index.html",title="Web Sitesi",user=user)
    