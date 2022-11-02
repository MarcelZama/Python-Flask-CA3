from flask import Flask, session, render_template, request
import os

app = Flask(__name__)
app.secret_key = (
    "kjhfdskjhfsdghk;odgkjsdkjsdkgsdgjdsghdjgdghdfghdfgdfghfggdf;uaghdfgagf"
)

@app.get("/")
def homepage():
    return render_template("index.html",title="Marcel Project")

@app.route("/info")
def info():
    return
    # return render_template("index.html",title="Marcel Project")

@app.route("/hobbies")
def hobbies():
    return
    # return render_template("index.html",title="Marcel Project")

@app.route("/cv")
def cv():
    return
    # return render_template("index.html",title="Marcel Project")

@app.route("/tehnologies")
def tehnologies():
    return
    # return render_template("index.html",title="Marcel Project")

if __name__ == "__main__":
    app.debug = True
    app.run()
