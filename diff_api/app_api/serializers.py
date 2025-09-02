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

    