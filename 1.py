from flask import Flask, session, render_template, request
import os

app = Flask(__name__)
app.secret_key = (
    "kjhfdskjhfsdghk;odgkjsdkjsdkgsdgjdsghdjgdghdfghdfgdfghfggdf;uaghdfgagf"
)


@app.get("/")
def homepage():
    return render_template("index.html", title="Marcel Project")


@app.route("/home")
def home():
    return render_template("index.html", title="Marcel Project")


@app.route("/info")
def info():
    return render_template("info.html", title="Marcel Project")


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", title="Marcel Project")


@app.route("/cv")
def cv():
    return render_template("cv.html", title="Marcel Project")


@app.route("/tehnologies")
def tehnologies():
    return render_template("tehnologies.html", title="Marcel Project")


@app.route("/tehno1")
def tehno1():
    return render_template("tehno1.html", title="Marcel Project")


@app.route("/tehno2")
def tehno2():
    return render_template("tehno2.html", title="Marcel Project")


@app.route("/tehno3")
def tehno3():
    return render_template("tehno3.html", title="Marcel Project")


if __name__ == "__main__":
    app.debug = True
    app.run()
