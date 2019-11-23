from django.shortcuts import render
from rest_framework import generics
from .models import Fruits
from .serializers import FruitsSerializer


class FruitsList(generics.ListCreateAPIView):
    queryset = Fruits.objects.all()
    serializer_class = FruitsSerializer


class FruitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruits.objects.all()
    serializer_class = FruitsSerializer

# Create your views here.
