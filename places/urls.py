"""
URL configuration for the favorite places app.

created on: 14/09/2026
created by: Daryna Bogaevska
"""

from django.urls import path

from . import views

app_name = "places"

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.place_list, name="place_list"),
    path("add/", views.place_add, name="place_add"),
]
