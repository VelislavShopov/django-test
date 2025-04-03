from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('users')