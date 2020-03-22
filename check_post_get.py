from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "DELETE"])
def check_request_type():
    return f"Wysłałeś {request.method} \n"


if __name__ == "__main__":
    app.run()