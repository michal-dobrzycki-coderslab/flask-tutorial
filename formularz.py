from flask import Flask
from flask import request

app = Flask(__name__)

formularz = """
<form action="/" method="POST">
    <label>
        Imię:
        <input type="text"
               name="user_name">
    </label>
    <button type="submit"> Wyślij </button>
</form>
"""


@app.route("/", methods=['POST','GET'])
def hello():
    if request.method=="POST":
        return f"Witaj {request.form['user_name']}"
    else:
        return formularz


if __name__ == "__main__":
    app.run()