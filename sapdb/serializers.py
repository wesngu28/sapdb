from rest_framework import serializers
from sapdb.models import Food, Pack, Use

class FoodSerializer(serializers.ModelSerializer):

  class Meta:
    model = Food
    fields = '__all__'

class PackSerializer(serializers.ModelSerializer):

  class Meta:
    model = Pack
    fields = '__all__'

class UseSerializer(serializers.ModelSerializer):

  class Meta:
    model = Use
    fields = '__all__'