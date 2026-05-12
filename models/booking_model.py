from database.db import db


class Booking(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    ride_id = db.Column(db.Integer, nullable=False)

    passenger_id = db.Column(db.Integer, nullable=False)

    booking_status = db.Column(db.String(50), default='confirmed')


    def __repr__(self):
        return f'<Booking {self.id}>'