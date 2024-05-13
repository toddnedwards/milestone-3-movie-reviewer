form moviereviewer import db


class Title(db.Model):
    #schema for Movie Title model
    id = db.Column(db.Integer, primary_key=True)
    title_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return self.title_name

class Genre(db.Model):
    #schema for task model
    genre_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        return self.category_name

    