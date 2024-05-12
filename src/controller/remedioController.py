from src.model.remedioModel import Remedio
import sqlite3

class RemedioController:
    
    def __init__(self):
        self.conexao = sqlite3.connect("remedios.db")
        self.cursor = self.conexao.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS remedios (nome text, quantidade integer, valor real)")
        self.conexao.commit()
    
    def listar(self):
        result=self.cursor.execute("SELECT * FROM remedios").fetchall()
        remedios:list[Remedio] = map(lambda x: Remedio(x[0], x[1], x[2]), result)
        print(result)
        return [remedio.to_dict() for remedio in remedios]
    
    def adicionar(self, remedio:Remedio):
        self.cursor.execute("INSERT INTO remedios VALUES (?,?,?)", (remedio.nome, remedio.quantidade, remedio.valor))
        self.conexao.commit()
        # self.remedios.append(remedio)
        
    def remover(self, remedio:Remedio):
        self.cursor.execute("DELETE FROM remedios WHERE nome = ?", (remedio.nome,))
        self.conexao.commit()
        # self.remedios.remove(remedio)
        