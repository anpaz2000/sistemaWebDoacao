from src.model.remedioModel import Remedio
import sqlite3

class RemedioController:
    
    def __init__(self):
        self.conexao = sqlite3.connect("doacoes.db")
        self.cursor = self.conexao.cursor()
        Remedio.setup(self)
    
    def listar(self):
        result=self.cursor.execute("SELECT * FROM remedios").fetchall()
        remedios:list[Remedio] = map(lambda x: Remedio(x[0], x[1], x[2]), result)
        print(result)
        return [remedio.to_dict() for remedio in remedios]
    
    def adicionar(self, remedio:Remedio):
        self.cursor.execute("INSERT INTO remedios VALUES (?,?,?)", (remedio.nome, remedio.quantidade, remedio.valor))
        self.conexao.commit()
        
    def remover(self, remedio:Remedio):
        self.cursor.execute("DELETE FROM remedios WHERE nome = ?", (remedio.nome,))
        self.conexao.commit()
        