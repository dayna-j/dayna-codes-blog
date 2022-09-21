from flask import Flask

application = Flask(__name__)

# from app import routes

@application.route("/")
def hello_world():
    return "<p>Hello, Wordld!</p>"

@application.route("/earth")
def hello_earth():
    return "<p>Hello, earth!</p>"

@application.route("/mars")
def hello_mars():
    return "<p>Hello, mars</p>"

if __name__ == "__main__":
    application.run(port=5000, debug=True)