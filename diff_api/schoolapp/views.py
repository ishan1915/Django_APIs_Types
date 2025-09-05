from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def login_view(request):
    serializers=LoginSerializer(data=request.data)
    
    if serializers.is_valid():
        username=serializers.validated_data['username']
        password=serializers.validated_data['password']
        user=authenticate(username=username,password=password)
        login(request,user)
        return Response({"msg":"login sucess"},status=200)
    return Response(serializers.errors)



@api_view(["POST"])
def signup_view(request):
    serializers=SignupSerializer(data=request.data)
    if serializers.is_valid():
        
        user=serializers.save()
        return Response(
            {"message": "User created successfully", "username": user.username, "email": user.email},
            status=status.HTTP_201_CREATED
        )
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)