from django.shortcuts import render

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer

from .tasks import transactions_read

# Create your views here.

class ReadDataView(APIView):
    
    def post(self, request):

        '''
            Post method for triggering the start of data imports from json file
        '''
 
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        path = serializer.data['file_path']
        credit_card_check = serializer.data['credit_card_check']

        transactions_read.delay(path, credit_card_check)
       
        data = {}
        data["success"] = True
        data["message"] = "File, (%s), will be read in"%(path)      
        return Response(data = data)


