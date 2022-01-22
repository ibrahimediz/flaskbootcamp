from app import app
from flask import Flask, render_template

@app.route("/")
@app.route("index")
def index():
    title = "Benim Projem"
    user = {"kullaniciadi":"Nedim can"}

    gonderiler = [
        {'yazar':{'username':'nedim'},
        'yazi':'merhaba dunya!'
        },
        {'yazar':{'username':'mert'},
        'yazi':'hi universe!'
        }]

    return render_template('index.html', title=title, user=user, gonderiler=gonderiler)