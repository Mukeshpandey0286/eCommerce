from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES = (
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
     ('Bihar','Bihar'),
     ('Chhattisgarh','Chhattisgarh'),
     ('Chandigarh','Chandigarh'),
     ('Dadra and Nagar Haveli and Daman & Diu','Dadra and Nagar Haveli and Daman & Diu'),
     ('Delhi', 'Delhi'),
     ('Goa','Goa'),
     ('Gujrat','Gujrat'),
     ('Haryana','Haryana'),
     ('Himanchal Pardesh', 'Himanchal Pardesh'), 
     ('Jharkhand','Jharkhand'),
     ('Karnataka', 'Karnataka'),
     ('Uttar Pradesh', 'Uttar Pradesh'),
     ('Uttarakhand', 'Uttarakhand'),
     ('West Bangal', 'West Bangal')
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def _str_(self):
        return str(self.id)


CATEGORY_CHOICES = (
       ('M', 'Mobile'),
       ('L', 'Laptop'),
       ('TW', 'Top Wear'),
       ('BW', 'Bottom Wear')
)
class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancle', 'Cancle')
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default= 'Pending')

