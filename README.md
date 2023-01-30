# Desafio Backend
Projeto realizado no sexto módulo do curso de **Formação em Desenvolvimento Full Stack da Kenzie Academy Brasil**

O objetivo desse projeto é desenvolver uma interface web que aceite upload de arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

## Linguagens utilizadas:
- HTML;
- Python.

## Bibliotecas e Frameworks utilizadas:
- Django;
- Django-Rest-Framework;
- uuid;
- python-dotenv.

### Clonando o repositório: 
1. Clique no botão verde escrito 'Code' acima e copie a chave SSH;
2. Abra o terminal dentro do repositório o qual você pretende salvar o projeto e execute o comando `git clone 'chave SSH'` (sem as aspas).

### Configurando o ambiente virtual e instalando as dependências do projeto (windows): 
1. Abra o terminal na pasta do projeto e execute `python -m venv venv`;
2. Depois rode o comando `.\venv\Scripts\activate` para entrar no ambiente virtual;
2. Por fim, ainda no terminal, escreva `pip install -r requirements.txt` para instalar as dependências. 

### Setando variáveis e rodando o projeto localmente:
1. Na pasta do projeto, crie uma copia do arquivo .env.example, mude o nome para .env e complete com as suas informações;
2. Rode o comando `python manage.py migrate` para executar as migrations;
3. Depois, rode o comando `python manage.py create_default_types` para criar o valores default do banco de dados;
4. Por fim, para rodar o servidor localmente, basta executar o comando `python manage.py runserver`.

