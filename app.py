from flask import Flask
from api import api
import os

app = Flask(__name__)
api.init_app(app)
# app.run(debug=True,host='0.0.0.0')
app.run(debug=True)
# if __name__ == '__main__':
