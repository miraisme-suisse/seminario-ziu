from flask import Flask, url_for
from api import api
import os

app = Flask(__name__)

api.init_app(app)
# app.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    app.run(debug=True)
