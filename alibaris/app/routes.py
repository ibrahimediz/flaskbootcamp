from app import app
from flask import render_template

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