from flask import Flask, url_for

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    return {
        "Usuário:": usuario,
        "Idade": idade,
        "Altura": altura,
    }

@app.route("/bemvindo")
def bem_vindo():
    return "<p>Bem vindo!</p>"


@app.route("/testedinamico/<usuario>")
def teste_dinamico(usuario):
    return f"<h1> Olá {usuario}, como vai?</h1>"

@app.route("/about", methods=["GET", "POST"])
def about():
    return "<h1>about page</h1>"

@app.route("/projects")
def projects():
    return "<h1>the project page</h1>"

with app.test_request_context():
    url = "/about"
    print(url_for("bem_vindo"))
    print(url_for("projects"))
    print(url_for("about", next="/"))
