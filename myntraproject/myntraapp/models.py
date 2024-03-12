from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomManager(models.Manager):
    def glass_list(self):
        return self.filter(category__exact="glass")

    def shoes_list(self):
        return self.filter(category__exact="Shoes")

    def cloth_list(self):
        return self.filter(category__exact="Cloths")

    def electronics_list(self):
        return self.filter(category__exact="Electronics")
    
    def getpricerange(self, r1, r2):
        return self.filter(price__range=(r1, r2))


class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    productid = models.IntegerField(primary_key=True)
    productname = models.CharField(max_length=55)
    type = (
        ("glass", "glass"),
        ("Cloths", "Cloths"),
        ("Shoes", "Shoes"),
        ("Electronics", "Electronics"),
    )
    category = models.CharField(max_length=50, choices=type, default="")
    desc = models.TextField(max_length=100)
    price = models.FloatField()
    photos = models.ImageField(upload_to="images")
    objects = models.Manager()
    productmanager = CustomManager()


class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    qty = models.PositiveIntegerField(default=0)


class Order(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    productid = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True
    )
    orderid = models.IntegerField(primary_key=True)
    qty = models.PositiveIntegerField(default=0)
