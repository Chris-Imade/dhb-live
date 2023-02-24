from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)
from .country import COUNTRY_LIST

class User(AbstractUser):
    GENDER_LIST = [("male", "female"), ("male", "male")]
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField('email address', unique = True)
    phone_number = models.CharField(max_length=100, blank=True,null=True)
    country = models.CharField(max_length=100, choices=COUNTRY_LIST, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='profile', null=True, blank=True)
    gender = models.CharField(choices=GENDER_LIST, max_length=50, null=True, blank=True, default="male")
    
    balance = models.IntegerField(help_text="Update user balance here... Ensure you insert the \
        right balance putting into consideration all transactions made... Do this after transactions have been approved..", default=0)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def __str__(self):
        return "{}".format(self.email)