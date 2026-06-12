from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://kartik:kartik123@flask.0wpqcoq.mongodb.net/?appName=flask"
)

db = client["testdb"]

users = db["users"]
todos = db["todos"]



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


@app.route("/todo")
def todo():
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    try:
        data = {
            "itemName": request.form["itemName"],
            "itemDescription": request.form["itemDescription"]
        }

        todos.insert_one(data)

        return """
        <h2>Todo Item Saved Successfully!</h2>
        <a href="/todo">Add Another Todo</a>
        """

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)