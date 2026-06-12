from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient(
    "mongodb+srv://kartik:kartik123@flask.0wpqcoq.mongodb.net/?appName=flask"
)

db = client["testdb"]
users = db["users"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = {
            "name": request.form["name"],
            "email": request.form["email"]
        }

        users.insert_one(data)

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("index.html", error=str(e))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)