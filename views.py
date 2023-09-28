from flask import Flask
from flask import Blueprint,  render_template , redirect , url_for

views = Blueprint(__name__, "views")
app = Flask(__name__, static_url_path='/static') 


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/go-to-home")
def go_to_home():
   return redirect(url_for("views.home"))

@views.route("/contact")
def contact():
    return "Contact US Today"

@views.route("/services")
def services():
    return "Check out our services"