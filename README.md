# Livraria MVP - Arquitetura MVC

Este projeto consiste na implementação de um MVP de uma livraria virtual, refatorado para a arquitetura MVC (Model-View-Controller). A aplicação permite a busca dinâmica de livros por categorias com uma interface moderna.

## Arquitetura do Projeto

Para atender aos requisitos do Exercício 2, o sistema foi dividido em três camadas fundamentais:

1. Model (models.py): Gerencia a fonte de dados e a lógica de filtragem.
2. View (templates/index.html): Interface do usuário desenvolvida com Tailwind CSS.
3. Controller (app.py): O motor Flask que orquestra as requisições.

## Funcionalidades Implementadas

- Arquitetura MVC: Separação física e lógica de componentes.
- Sugestão de Busca: Barra de pesquisa inteligente com dropdown de categorias.
- Front-end Funcional: Design responsivo inspirado em protótipos do Figma.

## Como Executar o Projeto

1. Criar o ambiente virtual:
```bash

python -m venv venv

```
2. Ativar o ambiente (Windows):
venv\Scripts\activate

3. Instalar dependências:
```bash
pip install -r requirements.txt
```

4. Rodar a Aplicação:
Entre no terminal da pasta e rode:
```bash
python app.py
```
Acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000)

5. Executar Testes BDD:
behave

## 📁 Estrutura de Pastas
├── app.py              
├── models.py           
├── templates/          
│   └── index.html      
├── features/           
├── requirements.txt    
└── README.md           
