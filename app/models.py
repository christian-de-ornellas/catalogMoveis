from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False,
                         unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
    # Compara o password e retorna true or false
    def compare_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User: {self.username}"

class Movie(db.Model):

    __tablename__ = "movies"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    brazilian_title = db.Column(db.String)
    year_of_production = db.Column(db.Integer)
    director = db.Column(db.String)
    genre = db.Column(db.String)

    def __init__(self, title, brazilian_title, year_of_production, director, genre):
        self.title = title
        self.brazilian_title = brazilian_title
        self.year_of_production = year_of_production
        self.director = director
        self.genre = genre

    def __repr__(self):
        return f"<Movie: {self.title}"


class Cast(db.Model):

    __tablename__ = "casts"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role = db.Column(db.String)
    name = db.Column(db.String)

    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    movie = db.relationship("Movie", foreign_keys=movie_id)

    def __init__(self, role, name):
        self.role = role
        self.name = name

    def __repr__(self):
        return f"<Cast: {self.role}"
