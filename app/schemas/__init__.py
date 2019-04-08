from flask_restful import fields
import json


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

casts_fields = {
    "id": fields.Integer,
    "role": fields.String,
    "name": fields.String,
    "movie_id": fields.Integer
}



list_casts_fields = {
    "role": fields.String,
    "name": fields.String,
}

resource_fields = {}
resource_fields['item'] = {}
resource_fields['item']['title'] = fields.String
resource_fields['item']['brazilian_title'] = fields.String
resource_fields['item']['year_of_production'] = fields.Integer
resource_fields['item']['director'] = fields.String
resource_fields['item']['genre'] = fields.String
resource_fields['cast']= {}
resource_fields['cast']['role'] = fields.String
resource_fields['cast']['name'] = fields.String

#resource_fields = {
#
#    "title": fields.String,
#    "brazilian_title": fields.String,
#    "year_of_production": fields.Integer,
#    "director": fields.String,
#    "genre": fields.String,
#    
#    "role": fields.String,
#    "name": fields.String,
#}