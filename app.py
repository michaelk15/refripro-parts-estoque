from flask import Flask, request, redirect

app = Flask(__name__)

pecas = []


@app.route("/")
def inicio():
    lista = ""

    for peca in pecas:
        lista += f"<li>{peca['nome']} - Quantidade: {peca['quantidade']}</li>"

    return f"""
    <h1>REFRIPRÓ PARTS</h1>
    <h2>Controle de Estoque</h2>

    <form action="/cadastrar" method="post">
        <label>Nome da peça:</label>
        <input type="text" name="nome" required>

        <label>Quantidade:</label>
        <input type="number" name="quantidade" min="0" required>

        <button type="submit">Cadastrar</button>
    </form>

    <h2>Peças cadastradas</h2>
    <ul>
        {lista}
    </ul>
    """


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])

    pecas.append({
        "nome": nome,
        "quantidade": quantidade
    })

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
