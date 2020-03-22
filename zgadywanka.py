from flask import Flask
from flask import request
import random


app = Flask(__name__)


formularz = """
<form action="/" method="POST">        
    <label>
    Wprowadź liczbę:
    <input type="number"
           name="zgadywanka">
    </label>
    <button type="submit">Zgadnij</button>
</form>
"""


los = random.randint(0, 100)


@app.route("/", methods=['GET', 'POST'])
def show_mainpage():
    if request.method=="GET":
        return formularz
    elif request.method=="POST":
        strzal = int(request.form["zgadywanka"])
        if los==strzal:
            return f"{los} : Gratulacje, udało Ci się!"
        elif los>strzal:
            return f" {los} za mało <hr>" + formularz
        else:
            return f" {los} za dużo <hr>" + formularz


if __name__ == "__main__":
    app.run()