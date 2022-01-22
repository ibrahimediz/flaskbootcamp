from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    gonderis = [{
        {"yazar": {"username": "bilal"},
        "eser": "sait faik'in abasıyanık kitabı :d"}
    }]

    return render_template('index.html', title="------", user=user, gonderiler=gonderis)