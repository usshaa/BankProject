from django.urls import path
from . import views


urlpatterns  = [
    path('',views.homePage,name='home'),
    path('home', views.homePage, name='home'),
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('landing',views.landingPage,name='landing'),
    path('message',views.messagePage,name='message'),
    path('form',views.application,name="form"),
]