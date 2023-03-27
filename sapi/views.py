from rest_framework.response import Response
from rest_framework.decorators import api_view
from sapdb.models import Food, Pack
from .serializers import FoodSerializer, PackSerializer

@api_view(['GET'])
def getFoods(request):
  foods = Food.objects.all()
  print(foods)
  serializer = FoodSerializer(foods, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getPacks(request):
  foods = Pack.objects.all()
  serializer = PackSerializer(foods, many=True)
  return Response(serializer.data)