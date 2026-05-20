from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    nome = dados["nome"]
    idade = dados["idade"]

    return jsonify({
        "mensagem": "Usuário cadastrado!",
        "nome": nome,
        "idade": idade
    })

if __name__ == "__main__":
    app.run(debug=True)