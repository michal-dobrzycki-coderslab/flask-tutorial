from flask import Flask
from datetime import datetime
#import datetime

app = Flask(__name__)


@app.route("/")
def show_mainpage():
    return '''
    <a href="/time">Kliknij żeby poznać czas [VIDEO, MEMY, WOW!]</a>
    <br />
    <a href="/date">Kliknij żeby poznać date [VIDEO, MEMY, WOW!]</a>
    '''


@app.route("/time")
def show_time():
    now = datetime.now().strftime("%H:%M:%S")
    return f"Jest {now}"


@app.route("/date")
def show_date():
    now = datetime.now().strftime("%d/%m/%Y")
    now2 = datetime.now().strftime("%Y-%m-%d")
    return f"Jest {now} albo {now2}"


if __name__ == "__main__":
    app.run()