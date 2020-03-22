from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/licz/<int:a>/<int:b>")
def dodawanie(a, b):
    return f"{a} + {b} = {a+b}"


@app.route("/licz")
def dodawanie_query():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        return f"query wynik {a} + {b} = {a + b}"
    except ValueError:
        return "parametry a oraz b muszą być liczbą"



if __name__ == "__main__":
    app.run()