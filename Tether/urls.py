# URLs for our app Tether

from django.urls import path
from Tether import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('register', views.register, name="registration_page"),
    path('login', views.loginUser, name="login_page"),
    path('logout', views.logoutUser, name="loggingemout"),
    path('campaigns', views.campaigns, name="campaigns_page"),
    path('about', views.about, name="about_page"),
    path('create', views.createCampaign, name="create_campaigns"),
    path('display/<int:id>/', views.displayCampaign, name="display_campaign"),
    path('createRegistration/<int:campaign_id>/', views.createRegistration, name="add_registration"),
    path('activity', views.activity, name="activities_page")
]