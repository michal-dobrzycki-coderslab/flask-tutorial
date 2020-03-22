from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def hello():
    if request.method=="POST":
        a = int(request.form["num_a"])
        b = int(request.form["num_b"])
        operation = request.form["operation"]
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "/":
            result = a / b
        elif operation == "*":
            result = a * b
        return f"a: {a}, b: {b}, result: {result}"
    else:
        return render_template("calc.html")


if __name__ == "__main__":
    app.run()