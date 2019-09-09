
from django.http import HttpResponse
from polls.models import Materials,Production
from polls.serializers import MaterialsSerializer,ProductionSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from master.models import item,customer,people,reports,inventory,sales,purchase
from master.serializers import itemSerializer,customerSerializer,peopleSerializer,reportsSerializer,inventorySerializer,salesSerializer,purchaseSerializer

def index(request):
    return HttpResponse("Hello!!! World")

class customerList(APIView):

    def get(self,request):
        customer1 = customer.objects.all()
        serializer = customerSerializer(customer1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class productionList(APIView):

    def get(self,request):
        production1 = Production.objects.all()
        serializer = ProductionSerializer(production1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class materialsList(APIView):

    def get(self,request):
        materials1 = Materials.objects.all()
        serializer = MaterialsSerializer(materials1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class itemList(APIView):

    def get(self,request):
        item1 = item.objects.all()
        serializer = itemSerializer(item1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class peopleList(APIView):

    def get(self,request):
        people1 = people.objects.all()
        serializer = peopleSerializer(people1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class reportsList(APIView):

    def get(self,request):
        report1 = reports.objects.all()
        serializer = reportsSerializer(report1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class inventoryList(APIView):

    def get(self,request):
        invent1 = inventory.objects.all()
        serializer = inventorySerializer(invent1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class salesList(APIView):

    def get(self,request):
        sales1 = sales.objects.all()
        serializer = salesSerializer(sales1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
