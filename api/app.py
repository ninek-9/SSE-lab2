from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/age")
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


@app.route("/git_user")
def github():
    return render_template("github.html")


@app.route("/submit", methods=["POST"])
def github_username():
    username = request.form.get("username")
    response = requests.get("https://api.github.com/users/{username}/repos")

    if response.status_code == 200:
        repos = response.json()
        return render_template("username.html",
                               name=username,
                               repositories=repos)

    else:
        return "GitHub API request failed."


def process_query(query):
    if "dinosaurs" in query:
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "name" in query:
        return "Nine Itti"
    elif "What is 43 plus 73?" in query:
        return "116"
    else:
        return "Unknown"


@app.route("/query")
def query():
    query_parameter = request.args.get("q")
    return process_query(query_parameter)


if __name__ == "__main__":
    app.run(debug=True)
