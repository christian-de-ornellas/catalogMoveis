#Catalogo de Filmes API

### Instalação

1. clonar o repositório
2. Abra um terminal com no diretorio da pasta onde você clonou a aplicação
3. Execute no terminal: **. venv/bin/activate** para acessar o ambiente virtual da aplicação
4. Execute no terminal: **venv/bin/pip3 install -r requirements.txt** para instalar as dependencias
5. Com o ambiente virtual ativado execute no terminal: **export FLASK_APP=main.py** para exportar as instancias ao shell flask.
6. Agora execute no terminal o comando: **flask shell** para acessar o shell.
7. No shell do flask execute o comando **db.create_all()** e um arquivo storage.db vai ser gerado na pasta app.
8. Abra o **SQLITE** e importe o arquivo storage.db que foi gerado dentro da pasta **app** com o nome de **storage.db**.
9. No terminal **aperte ctrl + d** para sair do shell e execute o comando **python3 main.py** para rodar a aplicação. 
10. Abra o postman, importe a collection. Obs: O arquivo de importação **Postman_collection.json** está na raiz do projeto.

### Como usar 

Obs: Você precisa acessar o Postman para acessar as rotas.

1. Você precisa criar um login clicando em **Auth/Register User**, clique em Body, adicione uma usuário e senha.

2. Com o login criado agora você precisa acessar **Auth/Login User** vá em *Body* coloque o seu usuário e senha e envie. Ao enviar você receberá um token de autenticação, copie o *token* que você vai precisar para acessar as rotas. 

3. Sempre que a API tem informar que você não tem permissão é porque **você precisa autenticar** com o token que você acabou de gerar, o **token tem válida de 10 minutos**. Quando a validade acabar você terá que gerar novamente.

4. Algumas rotas é *obrigatório a autenticação* e para isso você precisa clicar em **autorização/Authorization** selecionar o **type = Bearer Token** colar e salvar o seu token de autenticação. 

5. Acesse **Movies/ Save Movie** para salvar um filme, e com a autenticação efetuada acesse a Body, adicione os dados e envie.

6. Acesse **Casts/ Save Cast** para salvar seus personagens, lembrando que você terá que adicionar o id do seu filme em movie_id

7. Acesse **Catalog/catalog movies** para acessar os filmes e personagens.

## Agradecimentos
Venho agradecer a Deus, a addTech, a Telecine pela a oportunidade e também minha família pela força.
Não foi fácil mas me diverti muito programando em python, com certeza foi a minha primeira aplicação de muitas usando essa linguagem tão maravilhosa.

## Bibliotecas usadas

aniso8601==6.0.0
Click==7.0
Flask==1.0.2
Flask-Cors==3.0.7
Flask-RESTful==0.3.7
Flask-SQLAlchemy==2.3.2
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
pkg-resources==0.0.0
PyJWT==1.7.1
pytz==2018.9
six==1.12.0
SQLAlchemy==1.3.2
Werkzeug==0.15.2
