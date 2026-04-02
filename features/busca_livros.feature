Feature: Busca de livros por categoria
  Como um usuário
  Quero filtrar livros por gênero
  Para encontrar rapidamente o que me interessa

  Scenario: Filtrar livros por categoria de Suspense
    Given que o banco de dados possui livros de "Suspense" e "Romance"
    When o usuário solicita a categoria "Suspense"
    Then o sistema retorna 1 livro
    And o título do livro é "O Silêncio dos Inocentes"

  Scenario: Categoria sem resultados
    Given que o banco de dados possui livros de "Suspense" e "Romance"
    When o usuário solicita a categoria "Fantasia"
    Then o sistema retorna 0 livro