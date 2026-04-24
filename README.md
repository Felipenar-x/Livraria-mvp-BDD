#  Livraria MVP - Arquitetura MVC

Este projeto consiste na implementação de um MVP (Minimum Viable Product) de uma livraria virtual, refatorado para a arquitetura **MVC (Model-View-Controller)**. A aplicação permite a busca dinâmica de livros por categorias com uma interface moderna e funcional.

##  Arquitetura do Projeto

Para atender aos requisitos do **Exercício 2**, o sistema foi dividido em três camadas fundamentais, garantindo a separação de responsabilidades:

1.  **Model (`models.py`)**: 
    - Gerencia a fonte de dados (atualmente uma lista de 50+ títulos).
    - Contém a lógica de negócio para filtragem de categorias (suporta múltiplos filtros simultâneos).
2.  **View (`templates/index.html`)**: 
    - Interface do usuário desenvolvida com **Tailwind CSS**.
    - Implementa lógica de apresentação para sugestão de categorias e exibição de tags (pills).
3.  **Controller (`app.py`)**: 
    - O motor **Flask** que orquestra as requisições.
    - Captura os parâmetros da URL, aciona o Model e renderiza a View correspondente.

##  Funcionalidades Implementadas

- [x] **Arquitetura MVC**: Separação física e lógica de componentes.
- [x] **Filtro Multi-categoria**: Possibilidade de filtrar por mais de um gênero ao mesmo tempo.
- [x] **Sugestão de Busca**: Barra de pesquisa inteligente com dropdown de categorias.
- [x] **Front-end Funcional**: Design responsivo inspirado em protótipos do Figma.
- [x] **Qualidade com BDD**: Testes automatizados usando `behave` para garantir que a busca nunca quebre.

##  Como Executar o Projeto

### 1. Preparar o Ambiente
Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente (Windows)
venv\Scripts\activate

# Ativar o ambiente (Mac/Linux)
source venv/bin/activate