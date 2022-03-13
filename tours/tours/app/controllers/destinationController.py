from pkgutil import read_code
from flask import request, jsonify
from app.models.destinations import add_trek, get_all_treks, get_single_trek, delete_single_trek, update_single_trek
from app.controllers.constants import VALIDATION_ERR, CREATED, SUCCESS

from app.utils.decorators import token_required

def add_treks():
    data = request.get_json()
    try:
        title = data['title']
        days = data['days']
        total_cost = data['total_cost']
        difficulty = data['difficulty']
        # user id is optional to this endpoint
        user_id = None
        if 'uId' in data:
            user_id =  data['uId']

        if title and days and total_cost and difficulty:
            if add_trek(title, days, difficulty, total_cost, user_id):
                return jsonify(
                    message = "Successfully added trek destination", 
                    data = {
                        "title": title,
                        "days": days,
                        "total_cost": total_cost,
                        "difficulty": difficulty,
                        "user_id": user_id
                        }
                    ), SUCCESS

    except KeyError as err:
        return {"error": "You forgot {" + str(err) + "}"}, VALIDATION_ERR 
    
def get_treks():
    if get_all_treks():
        single_trek = []
        for treks in get_all_treks():
            new_treks={}
            new_treks['title'] = treks[1]
            new_treks['days'] = treks[2]
            new_treks['difficulty'] = treks[3]
            new_treks['uid'] = treks[6]
            new_treks['total_cost'] = treks[4]
            single_trek.append(new_treks)
        return jsonify(status="success", data = single_trek), SUCCESS

    return jsonify(stauts="success", data = []), SUCCESS


@token_required
def add_trek_destination(user):
    if request.method=="POST":
        return add_treks()
    if request.method == "GET":
        return get_treks()

@token_required
def single_trek_controller(user,id):
    if request.method == "GET":
        single_trek = get_single_trek(id)
        if single_trek:
            return jsonify(status="success", data={
                "title": single_trek[1],
                "days": single_trek[2],
                "difficulty": single_trek[3],
                "uid": single_trek[6],
                "total_cost": single_trek[4]
            })
        return jsonify(status="success", data = [])
    if request.method == "DELETE":
        if delete_single_trek(id):
            return jsonify(status="success", message="successfully deleted the trek"), SUCCESS
        return jsonify(status="failed", message="Could not find this ID"), VALIDATION_ERR

    if request.method == 'PUT':
        data = request.get_json()
        try:
            title = data['title']
            days = data['days']
            total_cost = data['total_cost']
            difficulty = data['difficulty']
            user_id =  data['uId'] 
            updated = update_single_trek(id, title, days, difficulty,total_cost,  user_id)
            if updated:
                return jsonify(
                    message = "Successfully updated trek destination", 
                    data = {
                        "title": title,
                        "days": days,
                        "total_cost": total_cost,
                        "difficulty": difficulty,
                        "user_id": user_id
                        }
                    ), SUCCESS
            return jsonify(message="failed", data=[]), SUCCESS
        except KeyError as err:
            return {"error": "You forgot {" + str(err) + "}"}, VALIDATION_ERR 

