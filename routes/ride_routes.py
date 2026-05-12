from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

from database.db import db

from models.ride_model import Ride
from models.booking_model import Booking

from utils.decorators import login_required


ride = Blueprint('ride', __name__)


@ride.route('/create-ride', methods=['GET', 'POST'])
@login_required
def create_ride():

    if session.get('user_role') != 'driver':

        flash('Only drivers can create rides!', 'danger')

        return redirect('/dashboard')


    if request.method == 'POST':

        pickup_location = request.form.get('pickup_location')

        destination = request.form.get('destination')

        departure_time = request.form.get('departure_time')

        available_seats = request.form.get('available_seats')

        fare = request.form.get('fare')


        new_ride = Ride(
            driver_id=session['user_id'],
            pickup_location=pickup_location,
            destination=destination,
            departure_time=departure_time,
            available_seats=available_seats,
            fare=fare
        )

        db.session.add(new_ride)
        db.session.commit()


        flash('Ride created successfully!', 'success')

        return redirect('/my-rides')


    return render_template('driver/create_ride.html')

@ride.route('/rides')
@login_required
def rides():

    all_rides = Ride.query.filter_by(status='active').all()

    return render_template('user/rides.html', rides=all_rides)


@ride.route('/book-ride/<int:ride_id>')
@login_required
def book_ride(ride_id):

    selected_ride = Ride.query.get_or_404(ride_id)


    if selected_ride.available_seats <= 0:

        flash('No seats available!', 'danger')

        return redirect('/rides')


    booking = Booking(
        ride_id=selected_ride.id,
        passenger_id=session['user_id']
    )


    selected_ride.available_seats -= 1


    db.session.add(booking)
    db.session.commit()


    flash('Ride booked successfully!', 'success')

    return redirect('/my-bookings')


@ride.route('/my-rides')
@login_required
def my_rides():

    driver_rides = Ride.query.filter_by(
        driver_id=session['user_id']
    ).all()


    return render_template(
        'driver/my_rides.html',
        rides=driver_rides
    )


@ride.route('/my-bookings')
@login_required
def my_bookings():

    bookings = Booking.query.filter_by(
        passenger_id=session['user_id']
    ).all()


    return render_template(
        'user/my_bookings.html',
        bookings=bookings
    )