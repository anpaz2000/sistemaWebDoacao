from flask import Flask
from flask import render_template, send_from_directory

from src.view.remedioView import RemedioView
app = Flask(__name__)

RemedioView(app)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)

    