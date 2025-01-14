from django.db import models
from django.contrib.auth.models import User

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

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.user} - {self.product.name}"

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    star = models.CharField(max_length=100, choices=STAR_CHOICES)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} rate {self.product.name}"