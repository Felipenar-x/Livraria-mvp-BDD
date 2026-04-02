import sys
from pathlib import Path
from behave import given, when, then

# Permite importar o código da pasta app
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))

from app.livraria import filtrar_livros


@given('que o banco de dados possui livros de "{cat1}" e "{cat2}"')
def step_impl(context, cat1, cat2):
    context.livros = [
        {"titulo": "O Silêncio dos Inocentes", "categoria": cat1},
        {"titulo": "Orgulho e Preconceito", "categoria": cat2},
    ]


@when('o usuário solicita a categoria "{categoria}"')
def step_impl(context, categoria):
    context.resultado = filtrar_livros(context.livros, categoria)


@then("o sistema retorna {qtd:d} livro")
def step_impl(context, qtd):
    assert len(context.resultado) == qtd


@then('o título do livro é "{titulo}"')
def step_impl(context, titulo):
    assert context.resultado[0]["titulo"] == titulo