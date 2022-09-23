from flask import Flask

application = Flask(__name__)

import routes

if __name__ == "__main__":
    application.run(port=5000, debug=True)

