from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    gonder =[{'yazar':{'username':'safiye'},
    'yazi':'Usmanım nereye gidersin'},
    {'yazar':{'username':'osman'},
    'yazi':'Elinin körüne giderim safiye'}]
    user = {"username" : "Çay var simit var neye bakıyon"}
    return render_template("index.html",title="Birine mi baktın baba yiğit",send=gonder)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.kullaniciadi.data, form.benihatirla.data))
        return redirect(url_for('index'))
    return render_template('login.html',title="Giriş Yap",form=form)