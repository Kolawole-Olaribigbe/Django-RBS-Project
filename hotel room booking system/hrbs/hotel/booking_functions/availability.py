import datetime
from hotel.models import Room, Booking

# Function to check room availability
def check_availability(room, check_in_date, check_out_date):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in_date > check_out_date or booking.check_out_date < check_in_date:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)