import uuid
from django.db import models
from django.contrib.auth.models import User


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.ManyToManyField('Type', related_name='item')
    size = models.ForeignKey('Size', related_name='item',
                             null='True', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True, null=True)

    def __str__(self):
        return f'Order: {self.createdAt.strftime("%b %d %I: %M %p")}'


class Carousel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class otherImages(models.Model):
    image = models.ImageField(upload_to='other_images/')
        
    def __img__(self):
        return self.image

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def totalPrice(self):
        cartmenuitems = self.cartmenuitems.all()
        total = sum([item.price for item in cartmenuitems])
        return total
    
    @property
    def totalItems(self):
        cartmenuitems = self.cartmenuitems.all()
        quantity = sum([item.quantity for item in cartmenuitems])
        return quantity

    
class CartMenuItem(models.Model):
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='item')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cartmenuitems") 
    quantity = models.IntegerField(default =0)

    def __str__(self):
        return self.MenuItem.name
    
    @property
    def price(self):
        newPrice = self.MenuItem.price * self.quantity
        return newPrice
    #hellur
    