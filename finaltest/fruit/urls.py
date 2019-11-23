from django.contrib import admin
from django.urls import path, include
from .views import FruitDetail,FruitsList
urlpatterns = [
    path("fruits/", FruitsList.as_view()),
    path("fruits/<int:pk>", FruitDetail.as_view())
]