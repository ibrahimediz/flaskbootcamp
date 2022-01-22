from hasan.app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    # data preperation
    title='Namımızın büyüklüyü dostlarımızın büyüklüğündendir'
    name='Süleyman Çakır'
    quotes=[["Atatürk","Everything we see in the world is the creative work of women"],
    ["Atatürk","Teachers are the one and only people who save nations"],
    ["Atatürk","Peace at Home, Peace in the World"]]

    return render_template('index.html',title=name,name=title,quotes=quotes)

