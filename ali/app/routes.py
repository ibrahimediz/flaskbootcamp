from app import app
from flask import render_template,flash,redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    gonderis = [
        {'yazar':{'username':'ali'},
        'yazi':'What a wonderful world'
        },
        {'yazar':{'username':'hasan'},
        'yazi':'Yakarsa dünyayı garipler yakar'
        },

    ]
    user = {"username":"Ali"}
    return render_template("index.html",title="Web Sitesi",user=user,gonderiler = gonderis)
@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():       
        return render_template("login.html",title="Giriş",form=form)