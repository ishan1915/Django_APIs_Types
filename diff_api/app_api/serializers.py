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



class SortSeializer(serializers.Serializer):
    numbers=serializers.ListField(
        child=serializers.FloatField(),min_length=1
    )


class ReverseSerializer(serializers.Serializer):
    numbers=serializers.ListField(
        child=serializers.FloatField()
    )

class SearchSerializer(serializers.Serializer):
    numbers=serializers.ListField(
        child=serializers.FloatField()
    )
    target=serializers.FloatField()

class MaxSerializer(serializers.Serializer):
    numbers=serializers.ListField(
        child=serializers.FloatField()
    )


class MinSerializer(serializers.Serializer):
    numbers=serializers.ListField(
        child=serializers.FloatField()
    )


class SumSerializer(serializers.Serializer):
    numbers=serializers.ListField(
        child=serializers.IntegerField()
    )


class Even(serializers.Serializer):
    numbers=serializers.ListField(
        child=serializers.FloatField()
    )