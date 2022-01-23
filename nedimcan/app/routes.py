from app import app
from flask import Flask, render_template, flash, redirect, url_for
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

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("{form.kullaniciadi.data} {form.benihatirla.data}", category="success")
        return redirect(url_for('index'))
    return render_template("login.html",title="Log-in",form=form)
