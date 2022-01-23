from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    gonderis = [
        {'yazar': {'username': 'berna',
        'yazi': 'düşün düşün aşamıyorum engelleri'},
         'yazar': {'username': 'ayse',
        'yazi': 'varamıyorum yanına çarelerin'}
        },
    ]
    user = {"kullaniciadi": "berna"}
    return render_template('index.html', gonderiler=gonderis, user=user)

@app.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.kullaniciadi.data, form.benihatirla.data))
        return redirect('/index')
    return render_template('login.html', title="Giriş Yap", form=form)
