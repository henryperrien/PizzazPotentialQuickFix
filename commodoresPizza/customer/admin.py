from django.contrib import admin
from .models import MenuItem, Size, Type, Order, Cart, CartMenuItem, Carousel

admin.site.register(MenuItem)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartMenuItem)
admin.site.register(Carousel)
