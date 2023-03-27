from rest_framework import serializers
from sapdb.models import Food, Pack

class FoodSerializer(serializers.ModelSerializer):

  class Meta:
    model = Food
    fields = '__all__'

class PackSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pack
    fields = '__all__'