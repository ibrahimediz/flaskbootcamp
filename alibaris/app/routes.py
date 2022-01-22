from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {"kullanici_adi":"Baris"}

    return render_template(
        'index.html', 
        title='Index', 
        user=user)