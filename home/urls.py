from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('support/', views.support, name ="support"),
    path('meditation/', views.meditation, name ="meditation"),
    path('journaling/', views.journaling, name ="journaling"),
    path('timetable/', views.timetable, name ="timetable"),
    path('therapy/', views.therapy, name ="therapy"),
    path('contact/', views.contact, name="contact"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog1/', views.blog1, name="blog1"),
    path('blog2/', views.blog2, name="blog2"),
    path('blog3/', views.blog3, name="blog3"),
    path('blog4/', views.blog4, name="blog4"),
    path('blog5/', views.blog5, name="blog5"),
    path('blog6/', views.blog6, name="blog6"),
    path('rec/', views.rec, name="rec"),
    path('recAdd/', views.recAdd, name="recAdd"),
    path('recUpdate/<str:id>/', views.recUpdate, name="recUpdate"),
    path('recDelete/<str:id>/', views.recDelete, name="recDelete"),
    path('blogAdd/', views.rec, name="blogAdd"),
    path('blogUpdate/', views.rec, name="blogUpdate"),
    path('profile/', views.profile, name="profile"),
    # path('login/', views.login, name="login"),
    # path('signup/', views.signup, name="signup"),

]
