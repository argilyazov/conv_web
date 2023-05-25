from rest_framework import serializers
from .models import *

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'

class ConvertorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convertor
        fields = '__all__'