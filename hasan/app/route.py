from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hi (Hola, Привет, Merhaba)'