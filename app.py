from flask import Flask, request, redirect

app = Flask(__name__)

pecas = []


@app.route("/")
def inicio():
    lista = ""

    for indice, peca in enumerate(pecas):
        lista += f"""
        <li>
            {peca['nome']} - Quantidade: {peca['quantidade']}
            <a href="/editar/{indice}">Editar</a>
            <a href="/excluir/{indice}">Excluir</a>
        </li>
        """

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


@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):
    if indice < 0 or indice >= len(pecas):
        return redirect("/")

    if request.method == "POST":
        pecas[indice]["nome"] = request.form["nome"]
        pecas[indice]["quantidade"] = int(request.form["quantidade"])
        return redirect("/")

    peca = pecas[indice]

    return f"""
    <h1>Editar peça</h1>

    <form method="post">
        <label>Nome da peça:</label>
        <input type="text" name="nome" value="{peca['nome']}" required>

        <label>Quantidade:</label>
        <input type="number" name="quantidade"
               value="{peca['quantidade']}" min="0" required>

        <button type="submit">Salvar</button>
    </form>

    <a href="/">Voltar</a>
    """


@app.route("/excluir/<int:indice>")
def excluir(indice):
    if 0 <= indice < len(pecas):
        pecas.pop(indice)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
