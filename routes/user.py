from flask import Blueprint,request, jsonify
from controllers.userController import get_all_user, create_user, update_user, delete_user

user_bp = Blueprint('users',__name__)

@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_user()
    return jsonify(user)

@user_bp.route('/', methods = ['POST'])
def store_user():
    data = request.get_json()
    name = data.get('name')
    email = data['email']
    password = data.get('password')
    print(f"variable name = {name}")
    print(f"variable email = {email}")
    print(f"variable pasword = {password}")

    new_user = create_user(name, email, password)
    return jsonify(new_user), 201

@user_bp.route('/<id>', methods = ['DELETE'])
def del_user (id):
    delete = delete_user(id)
    return jsonify(delete[0], delete[1])

@user_bp.route('/<id>', methods = ['PUT'])
def upd_user (id):
    data = request.get_json()
    name = data.get('name')
    email = data['email']
    password = data.get('password')
    update = update_user(id, name, email, password,)
    return jsonify(update), 200
