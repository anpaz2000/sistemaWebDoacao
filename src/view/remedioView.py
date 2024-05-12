from flask import render_template, request, jsonify
from src.controller.remedioController import RemedioController
from src.model.remedioModel import Remedio
class RemedioView:
    def __init__(self, app):
        self.app = app
        
        self.app.add_url_rule("/consulta", view_func=self.getRemedio, methods=["GET"])
        self.app.add_url_rule("/cadastro_remedio", view_func=self.cadastrarRemedioView, methods=["GET"])
        self.app.add_url_rule("/cadastrar_remedio", view_func=self.adicionar, methods=["POST"])
        
    def getRemedio(self):
        controller = RemedioController()
        remedios = controller.listar()
        return jsonify(remedios)
    
    def cadastrarRemedioView(self):
        return render_template("cadastro_remedio.html")
    
    def adicionar(self):
        controller = RemedioController()
        remedio = Remedio(request.json["nome"], request.json["quantidade"], request.json["valor"])
        controller.adicionar(remedio)
        return "Remedio adicionado com sucesso"