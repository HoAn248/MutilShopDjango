from django.db import models
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='product_images')
    date = models.DateTimeField(auto_now_add=True)
# Create your models here.
