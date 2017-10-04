from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Datapoint(db.Model):

    __tablename__ = 'datapoints'

    __table_args__ = (
        db.UniqueConstraint("freq", "name", "date"),
    )

    id = db.Column(db.Integer, nullable=False, 
                         unique=True, 
                         autoincrement=True,
                         primary_key=True)
    freq = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)


    value =db.Column(db.Float, nullable=False)
