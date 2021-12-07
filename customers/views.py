from django.shortcuts import render
from .models import Customers
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer
import pandas as pd
from .utility import date_converter

# Create your views here.


class ReadDataView(APIView):
    
    def post(self, request):

        '''
            Post method for triggering the start of data imports from json file
        '''
 
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        path = serializer.data['file_path']

        '''
            Read file using path
        '''
        df = pd.read_json(path)
        '''
            Apply data transformation to obtain dates in uniform fashion
        '''
        df['date_of_birth'] = df['date_of_birth'].transform(date_converter)

 

     
        return Response(data = {'status': 'Done'})