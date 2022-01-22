from app import app


from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'kullaniciadi': 'Orkun'}
    gonderiler = [
        {'yazar':{'username':'ali'},
        'yazi':'What a wonderful world'
        },
        {'yazar':{'username':'orkun'},
        'yazi':'Yaprak Dökümü'
        }
    ]
    return render_template('index.html', title='Web Projesi', user=user,gonderiler=gonderiler)

@app.route('/login')
def login():

    form = LoginForm()

    return render_tempate('login.html',title='Giriş Yap',form=form)