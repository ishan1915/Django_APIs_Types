from .models import *
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=10)
    password=serializers.CharField(max_length=10)



class SignupSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','email','password','confirm_password']

    def validate(self,data):
        if data['password'] !=data['confirm_password']:
            raise serializers.ValidationError("password not match")
        return data
        
    def create(self,validate_data):
        validate_data.pop('confirm_password')
        user=User.objects.create_user(**validate_data)
        return user
    


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
