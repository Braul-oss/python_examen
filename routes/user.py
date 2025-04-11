from flask import Blueprint,request, jsonify
from controllers.userController import get_all_user, create_user, update_user, delete_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('users',__name__)

@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_user()
    return jsonify(user)

@user_bp.route('/', methods=['POST'])
def store_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    result = create_user(name, email, password)
    return jsonify(result), 201

@user_bp.route('/<id>', methods = ['DELETE'])
def del_user (id):
    delete = delete_user(id)
    return jsonify(delete[0], delete[1])

@user_bp.route('/<id>', methods=['PUT'])
def upd_user(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    # Llamar a la función de actualización
    update = update_user(id, name, email, password)
    
    return jsonify(update), 200

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = login_user(email, password)
    if user:
        return jsonify({"message": "Login exitoso", "user": user}), 200
    else:
        return jsonify({"message": "Credenciales inválidas"}), 401