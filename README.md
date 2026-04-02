# Projeto Livraria MVP

Projeto simples usando BDD (Behavior-Driven Development) e desenvolvimento Top-Down.

## Funcionalidade
Filtrar livros por categoria (ex: Suspense).

## Como rodar

1. Criar ambiente virtual:
python -m venv venv

2. Ativar:
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

3. Instalar dependências:
pip install -r requirements.txt

4. Rodar os testes:
behave

## Estrutura
- app/livraria.py → lógica
- features/ → cenários BDD
- steps.py → implementação dos passos