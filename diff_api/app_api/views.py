from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
# 1. APIView – Low-Level Base Class
 
class HelloWorld(APIView):
    def get(self,request):
        return Response({"message":"Hello World"})


#2.Genric Views-For a single purpose-create,update,view,delete
#createAPI VIEW
class ItemCreateView(generics.CreateAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer


#RetriveAPI View-retrive single item
class ItemRetrieveView(generics.RetrieveAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

#ListAPI View-List all items
class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#UpdateAPIView ------
class ItemUpdateView(generics.UpdateAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer






