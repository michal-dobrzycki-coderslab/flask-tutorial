from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Witaj użytkowniku!"


@app.route("/hello/<imie>")
def hello_imie(imie):
    return f"Hello {imie}"
    #return "Hello " + imie


if __name__ == "__main__":
    app.run()