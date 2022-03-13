from crypt import methods
from flask import Flask,jsonify
from flask_mysqldb import MySQL
from os import environ
app = Flask(__name__)

app.config['MYSQL_HOST'] = environ.get('db_host')
app.config['MYSQL_USER'] = environ.get('db_user')
app.config['MYSQL_PASSWORD'] = environ.get('db_password')
app.config['MYSQL_DB'] = environ.get('db_name')
mysql = MySQL(app)

from app.routes import travel_app

app.register_blueprint(travel_app)

@app.route("/", methods=['get'])
def landing_page():
    return jsonify("welcome to the app ... ")



