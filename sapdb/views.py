from rest_framework.response import Response
from rest_framework.decorators import api_view
from sapdb.models import Food, Pack, Use
from .serializers import FoodSerializer, PackSerializer, UseSerializer

@api_view(['GET'])
def getFoods(request):
  foods = Food.objects.all()
  serializer = FoodSerializer(foods, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getPacks(request):
  foods = Pack.objects.all()
  serializer = PackSerializer(foods, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getUses(request):
  uses = Use.objects.all()
  serializer = UseSerializer(uses, many=True)
  return Response(serializer.data)