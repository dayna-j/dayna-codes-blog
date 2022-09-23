from flask import Flask
from application_blueprint import application_blueprint

application = Flask(__name__)

application.register_blueprint(application_blueprint)

if __name__ == "__main__":
    application.run(port=5000, debug=True)

