from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    nome = "popkiro"
    dados = {"Profissão":"Estudante", "Idade":"21"}

    return render_template('index.html', nome=nome, dados=dados)


@app.route('/contato') ### Sempre que eu quiser adicionar outra página, eu tenho que definir uma rota usando o @app.route('/') porém sempre colocar o nome da página após o contra barra, e lembrar de fechar com o '
def contato():
    return render_template('contato.html')