from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/medicamento")
def cadastrar_medicamentos():
    return render_template("Medicamentos.html")

@app.route("/consulta")
def consulta_de_medicamentos():
    return render_template("consulta_medicamento.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=105, debug=True)

    