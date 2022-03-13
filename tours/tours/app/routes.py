from flask import Blueprint
from app.controllers.AuthController import login, signup, add_to_db
from app.controllers.destinationController import add_trek_destination, single_trek_controller



travel_app = Blueprint('travel_app', __name__)

@travel_app.route('/login', methods=['GET'])
def do_login():
    return login()

@travel_app.route('/signup', methods=[ 'POST'])
def do_signup():
    return signup()

@travel_app.route('/trek', methods=['GET', 'POST'])
def add_trek():
    return add_trek_destination()

@travel_app.route('/trek/<id>', methods=['GET', 'DELETE', 'PUT'])
def get_trek(id):
    return single_trek_controller(id)