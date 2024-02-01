from .serializer import Drinkserializer
from .models import drinks
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.

@api_view(['GET','POST'])
def drink(request):
    if request.method == "GET":
        data = drinks.objects.all()
        serialized = Drinkserializer(data , many = True)
        return Response({'drinks': serialized.data})
    
    if request.method == "POST":
        serializer = Drinkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])    
def drink_detail(request,id):  
    try:
        drink = drinks.objects.get(pk=id)
    except drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized = Drinkserializer(drink)
        return Response({'drinks': serialized.data})
    
    elif request.method == 'PUT':
        serializer = Drinkserializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)