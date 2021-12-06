from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    fingerprint = models.CharField(max_length=100)

class FraudCheck(models.Model):
    fingerprint = models.CharField(max_length=100)
    ipaddr = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
