from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Email(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    subject = models.CharField(max_length=150)
    headers = models.TextField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)