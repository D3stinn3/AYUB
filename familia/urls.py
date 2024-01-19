from django.contrib import admin
from django.urls import path, include
from familia.views import homePage, truehomePage, adminPage, memberPage

urlpatterns = [
    path("", homePage, name="homepage"),
    path("homepage/", truehomePage, name="truehome"),
    path("adminpage/", adminPage, name="adminpage"),
    path("members/", memberPage, name="memberpage"),
]