from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    gonderis = [{
        {"yazar": {"username": "bilal"},
        "eser": "sait faikten abasıyanık"}
    }]

    return render_template('index.html', title="------", user=user, gonderiler=gonderis)