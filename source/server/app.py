import json
from flask.templating import render_template
from flask import Flask
from flask_bootstrap import Bootstrap

from .screen import screenlive


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def screen():
    return render_template("screen.html")


@app.route('/screenfeed/', methods=["POST"])
def screenfeed():
    return json.dumps([True, screenlive.gen().decode("utf-8")])
