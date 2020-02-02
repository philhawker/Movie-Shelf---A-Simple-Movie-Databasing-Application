from app import db


class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)


class Movie(db.Model):

    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    actor = db.Column(db.String)
    release_date = db.Column(db.String)
    rating = db.Column(db.String)
    genre_type = db.Column(db.String)

    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))
    actor = db.relationship("Actor", backref=db.backref(
        "movies", order_by=id), lazy=True)
