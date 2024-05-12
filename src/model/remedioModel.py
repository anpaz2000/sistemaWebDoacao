class Remedio:
    def __init__(self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def to_dict(self):
        return {'nome': self.nome, 'quantidade': self.quantidade, 'valor': self.valor}