import sqlite3

# cria banco usuario.db SQlite
conexao = sqlite3.connect('usuario.db')

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