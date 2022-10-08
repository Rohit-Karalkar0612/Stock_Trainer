from django.db import models
from User.models import Profile, Consultant, Subscribe
# Create your models here.
class Room(models.Model):
    reg_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=30)
    starts_in = models.TimeField()
    ends_in = models.TimeField()
    room_money = models.IntegerField()

    def __str__(self):
        return self.room_name

class Join(models.Model):
    reg_user_id = models.OneToOneField(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_money = models.IntegerField()

class Stock(models.Model):

    stock_name = models.CharField(max_length=10)
    nse_code = models.CharField(max_length=20)

    def __str__(self):
        return self.nse_code

class Buy(models.Model):

    reg_user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reg_room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    reg_stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    current_stock_price = models.IntegerField()
    no_of_shares = models.IntegerField()