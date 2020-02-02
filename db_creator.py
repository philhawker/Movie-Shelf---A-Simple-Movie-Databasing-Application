from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mymovies.db', echo=True)
Base = declarative_base()


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Actor: {}>".format(self.name)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)
    rating = Column(String)
    genre_type = Column(String)

    actor_id = Column(Integer, ForeignKey("actors.id"))
    actor = relationship("Actor", backref=backref(
        "movies", order_by=id))


Base.metadata.create_all(engine)