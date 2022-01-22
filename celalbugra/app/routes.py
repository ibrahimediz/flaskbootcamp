from app import app
from flask import render_template
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    # return "Hello World!"
    gonderis = [
        {'yazar':{'username':'ali'},
        'yazi':'What a wonderful world'},
        {'yazar':{'username':'hasan'},
        'yazi':'deneme'}
    ]
    
    user = {"kullaniciadi":"Bugra"}
    return render_template("index.html",title="Deneme",user=user,gonderiler=gonderis)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title="Giriş Yap",form=form)