import sqlite3

# cria banco usuario.db SQlite
conexao = sqlite3.connect('banco_de_dados.db')

# executar comandos SQL
cursor = conexao.cursor()

# criar a tabela de usuario
comando_sql = """
CREATE TABLE IF NOT EXISTS remedio (
	id	INTEGER PRIMARY KEY,
    nome	TEXT,
	quantidade	INTEGER,
	dosagem	TEXT,
	validade	DATE,
	id_usuario  INTEGER,
	FOREIGN KEY(id_usuario) REFERENCES usuario(id)
)
"""
# Executar o comando SQL
cursor.execute(comando_sql)

### Tabela usuario

# executar comandos SQL
cursor = conexao.cursor()

# criar a tabela de usuario
comando_sql = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    telefone TEXT,
    senha TEXT
)
"""
# Executar o comando SQL
cursor.execute(comando_sql)

# fechar a conexão
conexao.commit()
conexao.close()