from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    gonder =[{'yazar':{'username':'safiye'},
    'yazi':'Usmanım nereye gidersin'},
    {'yazar':{'username':'osman'},
    'yazi':'Elinin körüne giderim safiye'}]
    user = {"username" : "Çay var simit var neye bakıyon"}
    return render_template("index.html",title="Birine mi baktın baba yiğit",send=gonder)