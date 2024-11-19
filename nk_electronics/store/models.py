from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Category(models.Model):
    # main_category = models.ForeignKey(Main_category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField( max_length=200)
    code = models.CharField( max_length=100)
    
    def __str__(self):
        return self.name
    
class Filter_price(models.Model):
    FILTER_PRICE = (("1000 to 10000","1000 to 10000"),("10000 to 200000","10000 to 20000"),("20000 to 30000","20000 to 30000"),
                    ("30000 to 40000","30000 to 40000"),("40000 to 50000","40000 to 50000"),("50000 and More","50000 and More"))
    price = models.CharField(choices = FILTER_PRICE, max_length=100)
    
    
    def __str__(self):
        return self.price
    
class Product(models.Model):
    
    CONDITION = (("New", "New"), ("Old", "Old"))
    STOCKS = (("IN STOCK", "IN STOCK"), ("OUT OF STOCK", "OUT OF STOCK"))
    STATUS = (("Publish", "Publish"), ("Draft", "Draft"))
    
    unique_id = models.CharField(unique = True, max_length = 100, null = True, blank = True)
    image = models.CharField(max_length=500)
    name = models.CharField(max_length=500)  
    price = models.IntegerField()
    condition = models.CharField(choices = CONDITION, max_length=100)
    information = RichTextField()
    
    description = RichTextField()
    stocks = models.CharField(choices = STOCKS, max_length=100)
    status = models.CharField(choices = STATUS, max_length=100)
    created_date = models.DateTimeField(default = timezone.now)
    
    Categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_price, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime("75%Y%m%d23")+ str(self.id)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name



class Images(models.Model):
    image = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
   
class Tag(models.Model):
    name = models.CharField( max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
class Contact_us(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField( max_length=200)
    subject = models.CharField( max_length=300)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.email
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField( max_length=200)
    lastname = models.CharField( max_length=200)
    country = models.CharField( max_length=200)
    address = models.TextField()
    city = models.CharField( max_length=200)
    state = models.CharField( max_length=200)
    postalcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField( max_length=200)
    additional_info = models.TextField(blank = True)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField( max_length=500, null = True, blank = True)
    paid = models.BooleanField(default = False, null = True)
    date = models.DateTimeField(default=datetime.datetime.now)
    

    def __str__(self):
        return self.user.username
    
class Order_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    quantity = models.CharField( max_length=100)
    price = models.CharField( max_length=100)
    total = models.CharField( max_length=100)
    
    def __str__(self):
        return self.order.user.username