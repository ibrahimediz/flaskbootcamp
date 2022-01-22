from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    sents = [
        {'yazar':{'username':'Arda'},
        'yazi':'Yazi 1',
        },
        {'yazar':{'username':'Hasan'},
        'yazi':'Yazi 2',
        },
    ]
    user = {"kullaniciadi":"Arda"}
    return render_template("index.html", title="Web Sitesi", sents=sents, user=user)