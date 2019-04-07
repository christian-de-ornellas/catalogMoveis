from flask_restful import Resource, marshal
from app import request, db, app
from app.schemas import users_fields
from app.models import User


class LoginRouter(Resource):
    pass

class RegisterRouter(Resource):
    def post(self):
        credential = request.only(["username", "password"])

        try:
            user = User(credential["username"], credential["password"])
            db.session.add(user)
            db.session.commit()
            return marshal(user, users_fields, "user")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500    