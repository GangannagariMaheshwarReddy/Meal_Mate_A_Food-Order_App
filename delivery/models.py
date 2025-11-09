from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Restaurant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    picture = models.URLField(max_length=400, default='https://designshack.net/wp-content/uploads/Free-Simple-Restaurant-Logo-Template.jpg')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    price = models.FloatField()
    vegeterian = models.BooleanField(default=False)
    picture = models.URLField(max_length=400, default='https://www.indiafilings.com/learn/wp-content/uploads/2024/08/How-to-Start-Food-Business.jpg')

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart")
    items = models.ManyToManyField(Item, related_name="carts", blank=True)

    def total_price(self):
        total = 0.0
        for item in self.items.all():
            try:
                total += float(item.price)
            except:
                pass
        return round(total, 2)

    def __str__(self):
        return f"Cart of {self.customer.username}"
