from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.index, name="register"),
    path('dashboard/', views.index, name="dashboard"),
]