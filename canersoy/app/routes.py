from app import app
from flask import render_template
from pathlib import Path
import os

@app.route("/")
@app.route("/index")
def index():
    posts = [
        {"postWriter":{"name":"Name1","surname":"Surname1"},"postText":"Post 1"},
        {"postWriter":{"name":"Name2","surname":"Surname2"},"postText":"Post 2"}
    ]
    user=os.path.basename(Path(__file__).parents[1])
    return render_template("index.html",title="Home",user=user,posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title="Login",form=form)