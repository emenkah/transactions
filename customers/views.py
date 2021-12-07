from django.shortcuts import render
from .models import Customers
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class ReadDataView(APIView):
    
    def post(self, request):
        
        # serializer = UserSerializer(data=request.data)

        # serializer.is_valid(raise_exception=True)

        # user_obj = serializer.save()

        # #client = Client.objects.get(user__id=user_obj.id, timezone=timezone)
    
        # data = serializer.data
        # #data["ClientID"] =  client.uuid
     
        return Response(data = {'status': 'Done'})