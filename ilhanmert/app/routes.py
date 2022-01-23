from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    gonderis = [
        {'yazar':{'username':'ilhan'},
        'yazi':'deneme'
        },
        {'yazar':{'username':'mert'},
        'yazi':'deneme'
        },

    ]
    user = {"kullanicadi":"ilhan"}
    return render_template("index.html",title="Web Sitesi",user=user,gonderiler = gonderis)
    
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.kullaniciadi.data, form.benihatirla.data))
        return redirect(url_for('index'))
    return render_template('login.html',title="Giriş Yap",form=form)