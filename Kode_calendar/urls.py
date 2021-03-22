from django.urls import path

from django.contrib.auth import views as auth_views


from . import views  # from base import views

urlpatterns = [
    path("", views.home, name="home"),
    path("all/", views.all, name="all"),
]