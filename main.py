from flask import Flask
from flask import render_template, send_from_directory, request, redirect, url_for, jsonify, session
import sqlite3
import json

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
    if not session.get('nome'):
        return redirect(url_for('cadastro'))
    return render_template("cadastro_remedio.html")

@app.route("/consulta")
def consulta_de_medicamentos():
    if not session.get('nome'):
        return redirect(url_for('cadastro'))
    return render_template("consulta_medicamento.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/busca_remedio_base", methods=["POST"])
def busca_remedio_base():
    json_request = request.json
    print(json_request, json_request["nome_remedio"])
    nome_remedio = json_request["nome_remedio"]
    conn = sqlite3.connect('remedio.db')
    cursor = conn.cursor()    
    # Consultar os dados
    cursor.execute(f"SELECT * FROM remedio WHERE upper(nome) like '%{nome_remedio}%'")
    dados = cursor.fetchall()
    return jsonify(dados)

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
    nome = request.form['nome'].upper()
    quantidade = request.form['quantidade']
    dosagem = request.form['Dosagem do remédio']
    validade = request.form['Validade']
    descricao = request.form['Descricao']
    doador = session['nome']

    # conecta com SQLite.
    conn = sqlite3.connect('remedio.db')
    cursor = conn.cursor()
  
    # Inserir dados na tabela SQLite.
    cursor.execute('''INSERT INTO remedio (nome, quantidade, dosagem, validade, doador, descricao)
                      VALUES (?, ?, ?, ?, ?, ?)''', (nome, quantidade, dosagem, validade, doador, descricao))

    # Commit e fechar conexão
    conn.commit()
    conn.close()

   # redireciona para página sucesso.html
    return redirect(url_for('consulta_de_medicamentos'))

@app.route("/submit_login", methods=['POST'])
def submit_login():
    email = request.form['email']
    senha = request.form['senha']

    # Conecta com SQLite
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    # Consulta os dados
    cursor.execute("SELECT * FROM usuario WHERE email = ? AND senha = ?", (email, senha))
    dados = cursor.fetchall()

    # Fecha conexão com o banco de dados
    conn.close()

    if len(dados) > 0:
        session['nome'] = dados[0][1]
        session['email'] = email
        session['secret_key'] = 'chave_acesso'
        return redirect(url_for('consulta_de_medicamentos'))
    else:
        return redirect(url_for('login'))
        
if __name__=="__main__":
    app.secret_key = 'chave_acesso'
    app.run(host="0.0.0.0",port=9000, debug=True)
