from flask import Flask
from flask import render_template, send_from_directory, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Adiciona o icone nas páginas
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/cadastro_remedio")
def cadastrar_medicamentos():
    return render_template("cadastro_remedio.html")

@app.route("/consulta")
def consulta_de_medicamentos():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']

    # conecta com SQLite.
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    # Inserir dados na tabela SQLite.
    cursor.execute('''INSERT INTO usuario (nome, email, telefone, senha)
                      VALUES (?, ?, ?, ?)''', (nome, email, telefone, senha))

# Commit e fechar conexão
    conn.commit()
    conn.close()

   # redireciona para página sucesso.html
    return redirect(url_for('login'))

 # submit dos remedios

@app.route('/submit_remedio', methods=['POST'])
def submit_remedio():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    dosagem = request.form['Dosagem do remédio']
    validade = request.form['Validade']

    # conecta com SQLite.
    conn = sqlite3.connect('remedio.db')
    cursor = conn.cursor()
  
    # Inserir dados na tabela SQLite.
    cursor.execute('''INSERT INTO remedio (nome, quantidade, dosagem, validade)
                      VALUES (?, ?, ?, ?)''', (nome, quantidade, dosagem, validade))

# Commit e fechar conexão
    conn.commit()
    conn.close()

   # redireciona para página sucesso.html
    return redirect(url_for('consulta_de_medicamentos'))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=105, debug=True)

    