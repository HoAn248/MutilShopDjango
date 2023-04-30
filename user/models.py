from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
