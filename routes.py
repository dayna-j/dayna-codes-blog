from application import application

@application.route("/")
def hello_world():
    return "<p>Hello, Wordld!</p>"

@application.route("/earth")
def hello_earth():
    return "<p>Hello, earth</p>"

@application.route("/mars")
def hello_mars():
    return "<p>Hello, mars?</p>"

@application.route("/venus")
def hello_venus():
    return "<p>Hello, venus?</p>"