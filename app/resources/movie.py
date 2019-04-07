from flask_restful import Resource, marshal
from app.models import Movie
from app.schemas import movies_fields
from app import request, db
from app.decorator import jwt_required

class MovieRouter(Resource):

    def get(self):
        movies = Movie.query.all()
        return marshal(movies, movies_fields, "movies")

    @jwt_required
    def post(self, current_user):
        credential = request.only(["title", "brazilian_title", "year_of_production", "director", "genre"])

        try:
            movie = Movie(credential["title"], credential["brazilian_title"], credential["year_of_production"], credential["director"], credential["genre"])
            db.session.add(movie)
            db.session.commit()
            return marshal(movie, movies_fields, "movie")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500

    @jwt_required
    def delete(self, current_user):

        credential = request.only(["id"])

        movie = Movie.query.get(credential["id"])

        if not movie:
            return {"erro": "Filme não existe!"}
        try:
            db.session.delete(movie)
            db.session.commit()
            return marshal(movie, movies_fields, "movie")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500

    @jwt_required
    def put(self, current_user):
        
        credential = request.only(["id", "title", "brazilian_title", "year_of_production", "director", "genre"])
        movie = Movie.query.get(credential["id"])

        if not movie:
            return {"erro": "Filme não existe!"}
        try:
            movie.title = credential["title"]
            movie.brazilian_title = credential["brazilian_title"]
            movie.year_of_production = credential["year_of_production"]
            movie.director = credential["director"]
            db.session.add(movie)
            db.session.commit()
            return marshal(movie, movies_fields, "movie")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500         
                        