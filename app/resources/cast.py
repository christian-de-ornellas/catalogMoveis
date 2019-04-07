from flask_restful import Resource, marshal
from app.models import Cast
from app.schemas import casts_fields
from app import request, db
from app.decorator import jwt_required

class CastRouter(Resource):

    def get(self):
        casts = Cast.query.all()
        return marshal(casts, casts_fields, "casts")

    @jwt_required
    def post(self, current_user):
        credential = request.only(["role", "name", "movie_id"])

        try:
            cast = Cast(credential["role"], credential["name"], credential["movie_id"])
            db.session.add(cast)
            db.session.commit()
            return marshal(cast, casts_fields, "cast")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500

    @jwt_required
    def delete(self, current_user):

        credential = request.only(["id"])

        cast = Cast.query.get(credential["id"])

        if not cast:
            return {"erro": "Filme não existe!"}
        try:
            db.session.delete(cast)
            db.session.commit()
            return marshal(cast, casts_fields, "cast")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500

    @jwt_required
    def put(self, current_user):
        
        credential = request.only(["id", "role", "name", "movie_id"])
        cast = Cast.query.get(credential["id"])

        if not cast:
            return {"erro": "Filme não existe!"}
        try:
            cast.role = credential["role"]
            cast.name = credential["name"]
            cast.movie_id = credential["movie_id"]
            db.session.add(cast)
            db.session.commit()
            return marshal(cast, casts_fields, "cast")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500         
                        