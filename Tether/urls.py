# URLs for our app Tether

from django.urls import path
from Tether import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('register', views.register, name="registration_page"),
    path('login', views.loginUser, name="login_page"),
    path('logout', views.logoutUser, name="loggingemout")
]