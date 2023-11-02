from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Super USer info
# 1) cal, 123

# Regular user info
# 1) Hulk, smash
# 2) Nilsa, like
# 3) norva, hacienda14

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)
    
class Campaign(models.Model):
    title = models.CharField(max_length=100)
    campaign_type = models.TextField()
    description = models.TextField()
    doe = models.DateTimeField()
    tags_arr = models.JSONField()
    bgimg = models.ImageField(upload_to='images/', null=True, blank=True)
    contact_info = models.JSONField()

    def __str__(self):
        return str(self.title)
