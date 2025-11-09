from django.contrib import admin
from .models import Customer, Restaurant, Item, Cart

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Cart)
