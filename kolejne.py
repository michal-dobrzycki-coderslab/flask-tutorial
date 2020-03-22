from flask import Flask
from flask import request

app = Flask(__name__)


#http://127.0.0.1:5000/licz/23/32
@app.route("/licz/<int:a>/<int:b>")
def dodawanie(a, b):
    return f"{a} + {b} = {a+b}"


#http://127.0.0.1:5000/licz?a=4&b=8
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