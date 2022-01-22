from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user ={"kullaniciadi":"ilhan"}
    gonderis=[
        {
            'yazar':{'username':'ilhan'},
            'yazi': 'post1'
        },
        {
            'yazar':{'username':'mert'},
            'yazi': 'post2'
        },
    ]
    user={'kullaniciadi':'ilhan'}
    return render_template("index.html",title="Web sitesi", user=user, gonderiler=gonderis)