import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request
from flask_mail import Mail, Message

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///order.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
mail = Mail(app)

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

@app.route("/print")
def prints():
    return render_template("print.html")

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

@app.route("/email", methods=["POST"])
def email():
    name = request.form.get("name")
    email = request.form.get("email")
    painting = request.form.get("painting")
    place = request.form.get("place")

    db.execute("INSERT INTO ticket(name, email, painting, place) VALUES(?, ?, ?, ?)", name, email, painting, place)
    order = db.execute("SELECT id FROM ticket WHERE email = ?", email)
    m = ("Thank you {} Your purchase Complete. Monica will be incontact with you in the next 24 hours. Your order number is {}. Your print is {} which will be printed from {}. Please make your payment using venmo to @Monica-Evans-18. Please make your payment private and include your mailing address. When your payment is received your print will be ordered and sent to the address you have specified. You will receive a confirmation number and tracking number for your purchase. If you have any further questions please reach out to me at monicacs502021@gmail.com Thank you again, Monica ")
    s = m.format(name, order, painting, place)
    message = Message(s, recipients=[email])

    mail.send(message)

    return render_template("index.html")

@app.route("/style")
def style():
    return render_template("/style.html")
