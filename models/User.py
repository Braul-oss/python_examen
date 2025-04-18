from config import db

class Users(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable= False)
    email = db.Column(db.String(50), unique = True, nullable= False)
    password = db.Column(db.String(255), nullable= False)


    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "email":self.email,
            "password": self.password,
        }