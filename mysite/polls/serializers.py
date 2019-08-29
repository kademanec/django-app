from django.conf.urls import url, include
from django.contrib.auth.models import User
from polls.models import Production,Materials
from rest_framework import routers, serializers, viewsets

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = ['packers', 'operators', 'chargemen','shiftmen']

class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ['chem_soap_noodles', 'perfume', 'packing','machinery']
