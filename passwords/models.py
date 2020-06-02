from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passwords", null=True)
    account = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.account
