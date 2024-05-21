import os
from flask import Flask
from flask import render_template, send_from_directory, request, redirect, url_for, jsonify, session
from flask_cors import CORS
import json
from sqlalchemy import create_engine, text

app = Flask(__name__)
CORS(app)

engine = create_engine(os.getenv("POSTGRES_URL").replace("postgres://", "postgresql://"), echo=True)

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
    with engine.connect() as conn:
        # Consultar os dados
        resultados = conn.execute(text(f"""
            SELECT remedio.*, usuario.nome as nome_usuario, usuario.telefone, usuario.email 
            FROM remedio 
            JOIN usuario ON remedio.id_usuario = usuario.id
            WHERE remedio.nome ilike '%' || :nome_remedio || '%'
        """), {"nome_remedio": nome_remedio})
        dados = [list(r) for r in resultados]
        print("@@@@@")
        print(dados)
        # [
        #  [id, nome, quantidade, dosagem, validade, nome_doador, contato_doador],
        #  [id, nome, quantidade, dosagem, validade, nome_doador, contato_doador],
        #  [id, nome, quantidade, dosagem, validade, nome_doador, contato_doador]
        # ]
        return jsonify(dados)

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']

    # conecta com Postgres.
    with engine.connect() as conn:

        # Inserir dados na tabela Postgres.
        conn.execute(text('''INSERT INTO usuario (nome, email, telefone, senha)
                        VALUES (:nome, :email, :telefone, :senha)'''),
                        [{"nome": nome, "email": email, "telefone": telefone, "senha": senha}])
        conn.commit()

   # redireciona para página sucesso.html
    return redirect(url_for('login'))

 # submit dos remedios

@app.route('/submit_remedio', methods=['POST'])
def submit_remedio():
    nome = request.form['nome'].upper()
    quantidade = request.form['quantidade']
    dosagem = request.form['Dosagem do remédio']
    validade = request.form['Validade']
    id_usuario = session['id_usuario']

    # conecta com Postgres.
    with engine.connect() as conn:
  
        # Inserir dados na tabela Postgres.
        conn.execute(text('''INSERT INTO remedio (nome, quantidade, dosagem, validade, id_usuario)
                        VALUES (:nome, :quantidade, :dosagem, :validade, :id_usuario)'''), 
                        {"nome": nome, "quantidade": quantidade, "dosagem": dosagem, "validade": validade, "id_usuario": id_usuario})

        # Commit e fechar conexão
        conn.commit()

    # redireciona para página sucesso.html
    return redirect(url_for('consulta_de_medicamentos'))

@app.route("/submit_login", methods=['POST'])
def submit_login():
    email = request.form['email']
    senha = request.form['senha']

    # Conecta com Postgres
    with engine.connect() as conn:
        resultados = conn.execute(text("SELECT * FROM usuario WHERE email = :email AND senha = :senha"), {"email": email, "senha": senha})
        dados = [r for r in resultados]

        if len(dados) > 0:
            session['nome'] = dados[0][1]
            session['email'] = email
            session['id_usuario'] = dados[0][0]
            session['secret_key'] = 'chave_acesso'
            return redirect(url_for('consulta_de_medicamentos'))
        else:
            return redirect(url_for('cadastro'))
        
if __name__=="__main__":
    app.secret_key = 'chave_acesso'
    app.run(host="0.0.0.0",port=9000, debug=True)
