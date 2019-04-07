from flask_restful import fields

users_fields = {
    "id": fields.Integer,
    "username": fields.String
}

movies_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "brazilian_title": fields.String,
    "year_of_production": fields.Integer,
    "director": fields.String,
    "genre": fields.String
}