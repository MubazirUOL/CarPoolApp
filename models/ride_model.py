from database.db import db


class Ride(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    driver_id = db.Column(db.Integer, nullable=False)

    pickup_location = db.Column(db.String(200), nullable=False)

    destination = db.Column(db.String(200), nullable=False)

    departure_time = db.Column(db.String(100), nullable=False)

    available_seats = db.Column(db.Integer, nullable=False)

    fare = db.Column(db.Float, nullable=False)

    status = db.Column(db.String(50), default='active')


    def __repr__(self):
        return f'<Ride {self.id}>'