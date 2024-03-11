from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name= 'Salerno')

@app.route('/quemsomos')
def quemSomos():
    return render_template('whoweare.html')

@app.route('/contato')
def contato():
    return render_template('contact.html')