from django.urls import path
from .import views

urlpatterns = [
    path("loginPage/", views.loginPage, name="loginPage"),
    path("logoutPage/", views.logoutPage, name="logoutPage"),
    path("signupPage/", views.signupPage, name="signupPage"),
]