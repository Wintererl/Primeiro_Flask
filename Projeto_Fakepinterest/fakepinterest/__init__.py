from flask import Flask
from flask_sqlalchemy import SQLAlchemy #Traduz código SQL para python e facilita o uso de banco de dados
from flask_login import LoginManager # Flask exige segurança no site. Isso daqui possibilita um sistema de login
from flask_bcrypt import Bcrypt # Faz a criptografia

app = Flask(__name__) # Isso cria o site. É obrigatório e recomendado pra fazer primeiro
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' #cria um banco de dados sqlite com o nome comunidade
app.config["SECRET_KEY"] = 'a3190c717717b80582c2b580d8bc02528'

database = SQLAlchemy(app) #Cria o banco de dados usando sqlalchemy
b = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage" # View == route. São a msm coisa. É a view que gerencia o login. Pra onde o usuário vai quando nn tiver logado


from fakepinterest import routes