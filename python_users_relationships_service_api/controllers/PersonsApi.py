from flask import Blueprint
from app import app
from services.PersonsService import PersonsService
from flask import jsonify, request

persons_api = Blueprint('persons_api', __name__)

persons_service = PersonsService()

@persons_api.route('/persons', methods=['POST'])
def add_person():
    try:
        _json = request.json
        _name = _json['name']
        _age = _json['age']
        # validate the received values
        if _name and _age and request.method == 'POST':
            row = persons_service.add_person(_name, _age)
            resp = jsonify(row)
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@persons_api.route('/persons', methods=['GET'])
def get_all_persons():
    try:
        app.logger.info("in /persons")
        
        rows = persons_service.get_all_persons()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@persons_api.route('/persons/<string:name>', methods=['GET'])
def get_person_by_name(name):
    try:
        row = persons_service.get_person_by_name(name)
        # row = name
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@persons_api.route('/persons/<string:name>/friends', methods=['GET'])
def get_friends(name):
    try:
        row = persons_service.get_friends(name)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@persons_api.route('/persons/<string:name>/maybe-you-know', methods=['GET'])
def get_friends_from_my_friends(name):
    try:
        row = persons_service.get_friends_from_my_friends(name)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@persons_api.route('/persons/<string:name1>/<string:name2>', methods=['DELETE'])
def delete_from_my_friends(name1, name2):
    try:
        row = persons_service.delete_from_my_friends(name1, name2)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@persons_api.route('/persons/make_friend', methods=['POST'])
def make_friend():
    try:
        _json = request.json
        _name1 = _json['name1']
        _name2 = _json['name2']
        if _name1 and _name2 and request.method == 'POST':
            row = persons_service.make_friend(_name1, _name2)
            resp = jsonify(row)
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@persons_api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp