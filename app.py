from flask import Flask, render_template, request
from models import obter_livros, filtrar_livros

app = Flask(__name__)

@app.route('/')
def index():
    categoria = request.args.get('categoria') # Pega o gênero da URL
    todos_livros = obter_livros()
    livros_filtrados = filtrar_livros(todos_livros, categoria)
    
    return render_template('index.html', livros=livros_filtrados)

if __name__ == '__main__':
    app.run(debug=True)