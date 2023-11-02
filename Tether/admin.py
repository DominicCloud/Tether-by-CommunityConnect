from django.contrib import admin
from .models import Profile, Campaign, CampaignRegistration

# Register your models here.
admin.site.register(Profile)
admin.site.register(Campaign)
admin.site.register(CampaignRegistration)