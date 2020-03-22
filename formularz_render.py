from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def hello():
    if request.method=="POST":
        return f"Witaj {request.form['user_name']}"
    else:
        return render_template("formularz.html")


if __name__ == "__main__":
    app.run()