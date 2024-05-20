from django.db import models
from userauth.models import User

# Create your models here.

class RoomType(models.Model):
    ROOM_TYPE = (
    ('SIN', 'SINGLE ROOM'),
    ('FAM', 'FAMILY ROOM'),
    ('DEL', 'DELUXE ROOM'),
    
)
    room_type_id = models.IntegerField()
    room_type = models.CharField(max_length=12, choices=ROOM_TYPE)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f'{self.room_type} {self.price}'
    

class Room(models.Model):

    room_id = models.IntegerField()
    room_no = models.IntegerField()
    room_type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE )
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.room_id} {self.room_no}'
    
    def price(self):
        return self.room_type_id.price
    

class Booking(models.Model):
    PAYMENT_STATUS = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('cancelled', 'Cancelled'),
        ('initiated', 'Initiated'),
        ('failed', 'Failed'),
        ('refunding', 'Refunding'),
        ('refunded', 'Refunded'),
        ('unpaid', 'Unpaid'),
        ('expired', 'Expired')
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    no_of_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return f'{self.user} booked {self.room} from {self.check_in_date} to {self.check_out_date}'
