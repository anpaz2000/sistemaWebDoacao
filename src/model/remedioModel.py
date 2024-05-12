import sqlite3
class Remedio:
    def __init__(self, nome, quantidade, valor):
        
        self.conexao = sqlite3.connect("doacoes.db")
        self.cursor = self.conexao.cursor()
        
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        
    def setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS remedios (nome text, quantidade integer, valor real)")
        self.conexao.commit()

    def to_dict(self):
        return {'nome': self.nome, 'quantidade': self.quantidade, 'valor': self.valor}