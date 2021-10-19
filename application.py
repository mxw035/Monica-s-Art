import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/art")
def art():
    return render_template("art.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/buy")
def buy():
    return render_template("buy.html")

@app.route("/artloth")
def artloth():
    return render_template("artloth.html")

@app.route("/meg")
def meg():
    return render_template("meg.html")

@app.route("/sun")
def sun():
    return render_template("sun.html")

@app.route("/bag")
def bag():
    return render_template("bagend.html")

@app.route("/tom")
def tom():
    return render_template("tom.html")

@app.route("/tree")
def tree():
    return render_template("tree.html")

@app.route("/print")
def print():
    return render_template("print.html")

@app.route("/grayloth")
def grayloth():
    return render_template("grayloth.html")

@app.route("/sepialoth")
def sepialoth():
    return render_template("sepialoth.html")

@app.route("/oploth")
def oploth():
    return render_template("oploth.html")

@app.route("/gmeg")
def gmeg():
    return render_template("gmeg.html")

@app.route("/smeg")
def smeg():
    return render_template("smeg.html")

@app.route("/omeg")
def omeg():
    return render_template("omeg.html")

@app.route("/gbag")
def gbag():
    return render_template("gbag.html")

@app.route("/sbag")
def sbag():
    return render_template("sbag.html")

@app.route("/obag")
def obag():
    return render_template("obag.html")

@app.route("/gsun")
def gsun():
    return render_template("gsun.html")

@app.route("/ssun")
def ssun():
    return render_template("ssun.html")

@app.route("/osun")
def osun():
    return render_template("osun.html")

@app.route("/gtom")
def gtom():
    return render_template("gtom.html")

@app.route("/stom")
def stom():
    return render_template("stom.html")

@app.route("/otom")
def otom():
    return render_template("otom.html")

@app.route("/gtree")
def gtree():
    return render_template("gtree.html")

@app.route("/stree")
def stree():
    return render_template("stree.html")

@app.route("/otree")
def otree():
    return render_template("otree.html")
