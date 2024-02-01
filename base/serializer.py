from rest_framework import serializers
from .models import drinks

class Drinkserializer(serializers.ModelSerializer):
    class Meta:
        model = drinks
        fields = ['id','name','price']