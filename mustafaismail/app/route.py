from app import app


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

    return render_template('index.html', gonderiler = gonderis)

