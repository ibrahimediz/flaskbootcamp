from app import app


from flask import render_template


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
