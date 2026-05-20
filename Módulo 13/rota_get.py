from flask import Flask

app = Flask(__name__)

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return "Fala mano, API funcionando!"

if __name__ == "__main__":
    app.run(debug=True)