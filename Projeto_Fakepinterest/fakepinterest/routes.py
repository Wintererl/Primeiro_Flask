# Armazena as rotas (links) usados no projeto

from flask import url_for, render_template
from fakepinterest import app
from flask_login import login_required

@app.route("/") # Isso define todas as rotas possíveis e que serão usadas no site. Nesse caso, só vai ter a homepage
def homepage(): # Pra cada site a mais, tem que definir o link aqui (oq estiver dentro da função, vai ser o html do link)
    return  render_template("homepage") #Tudo que vai estar no site

@app.route("/perfil/<usuario>") # <usuário> é para que criar uma variável. Qlqr coisa que esteja na url no lugar vai ser uma url diferente
@login_required
def perfil(usuario): # A variável é passada como parâmetro pra função que define a rota. Gera DINAMICIDADE
    return render_template("perfil", usuario=usuario) # A variável é passada como argumento aqui. A variável recebe oq estiver na url