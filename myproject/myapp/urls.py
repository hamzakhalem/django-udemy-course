from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('second/', views.second, name="second"),
    path('add/<int:a>/<int:b>', views.add, name="add"),
]