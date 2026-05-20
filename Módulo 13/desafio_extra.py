from flask import Flask, request, jsonify

app = Flask(__name__)

posts = []

@app.route("/posts", methods=["GET"])
def listar_posts():
    return jsonify(posts)

@app.route("/posts", methods=["POST"])
def criar_post():
    dados = request.get_json()

    titulo = dados["titulo"]
    conteudo = dados["conteudo"]

    post = {
        "titulo": titulo,
        "conteudo": conteudo
    }

    posts.append(post)

    return jsonify({
        "mensagem": "Post criado!"
    })

if __name__ == "__main__":
    app.run(debug=True)