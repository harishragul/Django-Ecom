from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shop(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=200)
    shop_identity = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    approved = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=200)
    prime = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    collection = models.BooleanField(default=False, null=True, blank=True)
    nav_bar = models.BooleanField(default=False, null=True, blank=True)
    adds = models.BooleanField(default=False, null=True, blank=True)
    foot = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Require(models.Model):
    customer = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    file = models.FileField(upload_to='require/', blank=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.customer}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    old_price = models.FloatField(default=0)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    details = models.TextField(max_length=1000, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    approved = models.BooleanField(default=False, null=True, blank=True)
    new = models.BooleanField(default=False, null=True, blank=True)
    top = models.BooleanField(default=False, null=True, blank=True)
    adds = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    @property
    def imageURL(self):
        try:
            url = self.image.urls
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.customer} - {self.id} - {self.complete}"

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    packed = models.BooleanField(default=False, null=True, blank=True)
    shipped = models.BooleanField(default=False, null=True, blank=True)
    out_for_delivery = models.BooleanField(default=False, null=True, blank=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - {self.id}"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=6)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}"
