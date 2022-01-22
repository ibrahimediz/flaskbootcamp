from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Sen şimdi naneyi yimedin mi?"