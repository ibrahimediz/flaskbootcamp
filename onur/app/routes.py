from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

    gonderis = [
        {'yazar':{'username':'Onur'},
        'yazi':'Baba biz ne yaşadık ya'},             
        {'yazar':{'username':'Akyol'},
        'yazi':'Araba nerede? Para nerde?'},
    ]
    user = {"kullaniciadi":"Onur"}
    return render_template("index.html", title="TireTire", user=user, gonderiler=gonderis)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Giriş Yap", form=form)