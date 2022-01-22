from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {"kullanici_adi":"Baris"}

    posts = [
        {'yazar':{'username':'ali'},
        'yazi':'POST ONE',
        },
        {'yazar':{'username':'baris'},
        'yazi':'POST TWO',
        },
        {'yazar':{'username':'alibaris'},
        'yazi':'POST THREE',
        },
    ]

    return render_template(
        'index.html', 
        title='Blog', 
        user=user,
        posts = posts,
        )

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requestek for user")

    return render_template('login.html',title="Login",form=form)