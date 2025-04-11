from models.User import Users
from config import db
from werkzeug.security import generate_password_hash, check_password_hash



def get_all_user():
    user = Users.query.all()
    print(user)

    return [
        user.to_dict()
    
    for user in Users.query.all()]

#def create_user(name, email, password):
    #print(f"user controller{name}")
    #new_user = Users(name, email, password)
    #db.session.add(new_user)
    #db.session.commit()
    #return new_user.to_dict()

def create_user(name, email, password):
    hashed_password = generate_password_hash(password)
    new_user = Users(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return {"message": "Usuario creado exitosamente"}

def delete_user(id):
    user_delete = Users.query.get(id)
    print(f"id del registro, {user_delete}")

    if user_delete:
        user_deleted = user_delete.to_dict()

        db.session.delete(user_delete)
        db.session.commit()
        return user_deleted, 200
    
    else:
        return {"error:" "usuario no encontrado"}, 404
    
def update_user(id, name, email, password):
    user_update = Users.query.get(id)
    user_update.name = name
    user_update.email = email
    
    # Encriptar la nueva contraseña antes de actualizarla
    hashed_password = generate_password_hash(password)
    user_update.password = hashed_password
    
    db.session.commit()
    return {"message": "Usuario actualizado exitosamente", "user": user_update.to_dict()}

def login_user(email, password):
    user = Users.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return {"id": user.id, "name": user.name, "email": user.email}
    return None