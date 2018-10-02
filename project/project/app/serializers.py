from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Equipo
# Mongo
from rest_framework_mongoengine import serializers as mongoserializers

class EquipoSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
##End Mongo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')