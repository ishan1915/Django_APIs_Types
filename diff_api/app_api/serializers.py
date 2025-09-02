from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price']


#calculator app #####################

class AddSerializer(serializers.Serializer):
    num1=serializers.FloatField()
    num2=serializers.FloatField()



class SubSerializer(serializers.Serializer):
    num1=serializers.FloatField()
    num2=serializers.FloatField()


class MulSerializer(serializers.Serializer):
    num1=serializers.FloatField()
    num2=serializers.FloatField()

class DivSerializer(serializers.Serializer):
    num1=serializers.FloatField()
    num2=serializers.FloatField()




class FactorialSerializer(serializers.Serializer):
    num=serializers.IntegerField()


class PowSerializer(serializers.Serializer):
    base=serializers.IntegerField()
    exponent=serializers.IntegerField()

    

