from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.run()

@app.route("/curso")
def curso():
    return "<h1>Eu faço curso de Técnio em Desenvolvimento de Sistemas!</h1>"
if __name__ == "__main__":
    app.run()
