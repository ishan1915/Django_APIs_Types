from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path
from rest_framework import generics
from .models import Item
from .serializers import *
from rest_framework import viewsets
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework import status
import math




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


def item_create_form(request):
    return render(request, 'item_create.html')  #for frontend template     


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

#login
def login_page(request):
    return render(request, 'login.html')

#dashboard
def dashboard_view(request):
    username = request.session.get('username')
    if username:
        return render(request, 'dashboard.html', {'username': username})
    return redirect('login_page')







#######calculator views########################
@api_view(['POST'])
def add_view(request):
    serializers=AddSerializer(data=request.data)
    if serializers.is_valid():
        return Response({"result":serializers.validated_data['num1']+serializers.validated_data['num2']})
    return Response(serializers.errors)


@api_view(['POST'])
def sub_view(request):
    serializers=SubSerializer(data=request.data)
    if serializers.is_valid():
        result=serializers.validated_data['num1']-serializers.validated_data['num2']
        return Response(result)
    return Response(serializers.errors)


@api_view(['POST'])
def mul_view(request):
    serializers=MulSerializer(data=request.data)
    if serializers.is_valid():
        result=serializers.validated_data['num1']*serializers.validated_data['num2']
        return Response(result)
    return Response(serializers.errors)



@api_view(["POST"])
def div_view(request):
    serializers=DivSerializer(data=request.data)
    if serializers.is_valid():
        result=serializers.validated_data['num1']/serializers.validated_data['num2']
        return Response(result)
    return Response(serializers.errors)



@api_view(['POST'])
def fact_view(request):
    serializers=FactorialSerializer(data=request.data)
    if serializers.is_valid():
        num=serializers.validated_data['num']
        result=math.factorial(num)
        return Response(result)
    return Response(serializers.errors)




@api_view(['POST'])
def pow_view(request):
    serializers=PowSerializer(data=request.data)
    if serializers.is_valid():
        base=serializers.validated_data['base']
        exponent=serializers.validated_data['exponent']
        result=math.pow(base,exponent)
        return Response(result)
    return Response(serializers.errors)




@api_view(['POST'])
def sort_view(request):
    serializers=SortSeializer(data=request.data)
    if serializers.is_valid():
        numbers=serializers.validated_data['numbers']
        result=sorted(numbers)
        return Response(result)
    return Response(serializers.errors)


@api_view(['POST'])
def reverse_view(request):
    serializers=ReverseSerializer(data=request.data)
    if serializers.is_valid():
        numbers=serializers.validated_data['numbers']
        result=reversed(numbers)
        return Response({"reversed numbers are":result})
    return Response(serializers.errors)


@api_view(["POST"])
def search_view(request):
    serializers=SearchSerializer(data=request.data)
    if serializers.is_valid():
        numbers=serializers.validated_data['numbers']
        target=serializers.validated_data['target']
        result=target in numbers
        if result==1:   
            return Response({"msg":"number is founded"})
        else:
           return Response({"msg":"number not in list"})

         
    return Response(serializers.errors)



@api_view(["POST"])
def max_view(request):
    serializers=MaxSerializer(data=request.data)
    if serializers.is_valid():
        numbers=serializers.validated_data['numbers']
        result=max(numbers)
        return Response({"the largest number:":result})
    return Response(serializers.errors)


@api_view(["POST"])
def min_view(request):
    serializers=MinSerializer(data=request.data)
    if serializers.is_valid():
        numbers=serializers.validated_data['numbers']
        result=min(numbers)
        return Response({"thesmallestnumberis":result})
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def sum_view(request):
    serializers=SumSerializer(data=request.data)
    if serializers.is_valid():
        numbers=serializers.validated_data['numbers']
        result=sum(numbers)
        return Response(result)
    return Response(serializers.errors)



@api_view(['POST'])
def even_view(request):
    even_num=[]
    serializers=Even(data=request.data)
    if serializers.is_valid():
        numbers=serializers.validated_data['numbers']
        for n in numbers:
            if n%2==0:
                even_num.append(n)
        return Response(even_num)
    return Response(serializers.errors)