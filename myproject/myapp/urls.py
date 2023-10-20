from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('imagepage/', views.imagepage, name="imagepage"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
    path('second/', views.second, name="second"),
    path('myform/', views.myform, name="myform"),
    path('submitform/', views.submitform, name="submitform"),
    path('newform/', views.newform, name="newform"),
]