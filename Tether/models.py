from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Super USer info
# 1) cal, 123

# Regular user info
# 1) Hulk, smash
# 2) Nilsa, like

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)