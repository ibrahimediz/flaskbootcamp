from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {"kullaniciadi": "berna"}
    return render_template('index.html', title="Web projesi", user=user)