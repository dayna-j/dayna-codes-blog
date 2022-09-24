from application import application
from flask import render_template

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/earth")
def hello_earth():
    return "<p>Hello, earth</p>"

@application.route("/mars")
def hello_mars():
    return "<p>Hello, mars?</p>"

@application.route("/venus")
def hello_venus():
    return "<p>Hello, venus?</p>"