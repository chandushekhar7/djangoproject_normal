
from django.urls import path
from app1 import views
urlpatterns = [
    path('home/',views.home),
    path('home2/',views.home2),
    path('di/',views.m1),
]
