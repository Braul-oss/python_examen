from models.User import Users
from config import db

def get_all_user():
    user = Users.query.all()
    print(user)

    return [
        user.to_dict()
    
    for user in Users.query.all()]

def create_user(name, email, password):
    print(f"user controller{name}")
    new_user = Users(name, email, password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

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
    user_update.password = password
    db.session.commit()
    return user_update.to_dict()