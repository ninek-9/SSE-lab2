from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/calculate_age", methods=["POST"])
def calculate_age():
    input_name = request.form.get("name")
    input_dob = request.form.get("dob")

    dob_date = datetime.strptime(dob, "%Y-%m-%d")

    today = datetime.now()
    age_in_days = (today - dob_date).days

    return render_template("hello.html", name=input_name, dob=input_dob)
