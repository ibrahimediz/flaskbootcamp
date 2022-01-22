from app import app
from flask import render_template
from pathlib import Path
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",title="Home Page",user=os.path.basename(Path(__file__).parents[1]))