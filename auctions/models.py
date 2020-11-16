from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class Product(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "auctioneer")
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image  = models.URLField(max_length = 500)
    baseprice = models.FloatField()
    date = models.DateTimeField()
    active = models.BooleanField()

class Bids(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE,related_name = "bidamount")
    amount = models.FloatField()

class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "comment")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "user_comment")
    comment = models.TextField()

class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "my_watchlist")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
