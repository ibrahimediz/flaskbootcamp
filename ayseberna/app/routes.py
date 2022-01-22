from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    gonderis = [
        {'yazar': {'username': 'berna',
        'yazi': 'düşün düşün aşamıyorum engelleri'},
         'yazar': {'username': 'ayse',
        'yazi': 'varamıyorum yanına çarelerin'}
        },
    ]
    user = {"kullaniciadi": "berna"}
    return render_template('index.html', gonderiler=gonderis, user=user)