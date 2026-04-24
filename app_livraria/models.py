from django.db import models

# Create your models here.
def filtrar_livros(lista_livros, categoria_alvo):
    """
    Retorna apenas os livros da categoria escolhida.
    """
    return [livro for livro in lista_livros if livro["categoria"] == categoria_alvo]