from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg    

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=1, max_digits=7)
    category = models.ManyToManyField(Category)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    @property
    def get_rating(self):
        return self.review_set.aggregate(avg_rating=Avg("star"))["avg_rating"] or 0

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.user} - {self.product.name}"

STAR_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    star = models.IntegerField(choices=STAR_CHOICES)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} rate {self.product.name}"