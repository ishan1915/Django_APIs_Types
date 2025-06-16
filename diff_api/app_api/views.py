from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework import status




# Create your views here.
# 1. APIView – Low-Level Base Class
# Use to write all different types of queries for like login,signup,custom logic,calling external apis,file uploading,handle multiple model
 
class HelloWorld(APIView):
    def get(self,request):
        return Response({"message":"Hello World"})

class ItemStatsAPIView(APIView):
    def get(self, request):
        total_items = Item.objects.count()
        total_price = Item.objects.aggregate(Sum('price'))['price__sum']
        return Response({
            'total_items': total_items,
            'total_price': total_price
        })


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

#UpdateAPIView 
class ItemUpdateView(generics.UpdateAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

#DestroyAPIView
class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


#3.Combo Genrics Views
#a-ListCreateAPI View

class ItemListCreateView(generics.ListCreateAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

#b.-RetrieveUpdateDestroyAPIView
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



#4.Viewsets
#a.modelViewSet-ModelViewSet, which is very powerful in Django REST Framework.
#It automatically gives you:

#List
#Retrieve
#Create
#Update
#Delete

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

#b. ReadOnlyModelViewSet
#only support Get-retrieve

class ItemReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


#5. Mixins + GenericAPIView (Custom Combo)
 


class ItemCustomView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)



#6Function Based api view
@api_view(['GET'])
def simple_viewa(request):
    return Response({"msg": "Hi from FBV"})



@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        request.session['username'] = user.username  # store username in session
        return redirect('dashboard')
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

def login_page(request):
    return render(request, 'login.html')

def dashboard_view(request):
    username = request.session.get('username')
    if username:
        return render(request, 'dashboard.html', {'username': username})
    return redirect('login_page')