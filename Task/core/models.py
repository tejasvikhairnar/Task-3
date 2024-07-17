from django.db import models
from django.contrib.auth.models  import AbstractUser
from .manager import UserManager



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    email_token = models.EmailField()
    forget_password = models.CharField(max_length=100)
    last_login_time = models.DateTimeField(null=True,blank=True)
    last_logout_time = models.DateTimeField(null= True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
# Create your models here.
