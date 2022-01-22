from app import app
from flask import Flask, render_template
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    title = "Benim Projem"
    user = {"kullaniciadi":"Nedim can"}

    gonderiler = [
        {'yazar':{'username':'nedim'},
        'yazi':'merhaba dunya!'
        },
        {'yazar':{'username':'mert'},
        'yazi':'hi universe!'
        }]

    return render_template('index.html', title=title, user=user, gonderiler=gonderiler)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title="Log-in",form=form)
