from app import app
from flask import render_template
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
    user = {"kullanicadi":"ibrahim"}
    return render_template("index.html",title="Web Sitesi",user=user,gonderiler = gonderis)
    
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title="Giriş Yap",form=form)