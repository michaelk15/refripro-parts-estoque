from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "REFRIPRÓ PARTS - Sistema de Controle de Estoque"


if __name__ == "__main__":
    app.run(debug=True)
