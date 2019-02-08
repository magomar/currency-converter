import requests

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

API_URL = "https://api.exchangeratesapi.io/latest"
currencies = ["EUR"]
res = requests.get(API_URL)
if res.status_code != 200:
    raise Exception("ERROR: API request unsuccessful.")
data = res.json()
rates = data["rates"]
for rate in rates:
    currencies.append(rate)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", currencies=currencies)
    else:
        amount = float(request.form.get("amount"))
        source = request.form.get("source")
        target = request.form.get("target")
        payload = {"base": source, "symbols": target}
        res = requests.get(API_URL, params=payload)
        app.logger.info(res)
        if res.status_code != 200:
            raise Exception("ERROR: API request unsuccessful.")
        data = res.json()
        app.logger.info(data)
        result = amount * data['rates'][target]
        return render_template(
            "index.html", currencies=currencies, source=source, target=target, amount=amount, result=result
        )

