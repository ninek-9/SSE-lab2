from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate_age", methods=["POST"])
def calculate_age():
    name = request.form.get("name")
    dob = request.form.get("dob")

    dob_date = datetime.strptime(dob, "%Y-%m-%d")

    today = datetime.now()
    age_in_days = (today - dob_date).days

    return render_template("hello.html", name=name, age_in_days=age_in_days)


def process_query(query):
    if "dinosaurs" in query:
        return "Dinosaurs ruled the Earth 200 million years ago"
    if "name" in query:
        return "Nine"
    else:
        return "Unknown"

    
@app.route("/query")
def query():
    query_parameter = request.args.get("q")
    return process_query(query_parameter)


if __name__ == "__main__":
    app.run(debug=True)
