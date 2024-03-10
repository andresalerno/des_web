# importa a classe flask
from flask import Flask, render_template


# cria uma instancia dessa classe)
app = Flask(__name__)

# cria rotas com o decorator
@app.route('/')
# funcao para retornar uma mensagem
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('whoweare.html')

@app.route('/contato')
def contact():
    return render_template('contact.html')