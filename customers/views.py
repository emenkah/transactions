from django.shortcuts import render
from .models import Customers
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer
import pandas as pd
from .utility import date_converter, age_computer

# Create your views here.

# def get_data(df, ind):
#     new_entry = Customers.objects.create(
#                 name=df.name[ind],
#                 address=df.address[ind],
#                 checked=df.checked[ind],
#                 description=df.description[ind],
#                 interest=df.interest[ind],
#                 date_of_birth=df.date_of_birth[ind],
#                 email=df.email[ind],
#                 account=df.account[ind],
#                 credit_card=df.credit_card[ind]
                
#                 )
#     new_entry.save()
#     # print("in Get data")
#     # print("Map entries", new_entry)
#     # return 

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

        print(df)
        last_two_records = Customers.objects.filter().order_by('id')[:2]
        print(list(last_two_records))
        
        last_but1_record = last_two_records[0]
        last_record = last_two_records[1]
        print(last_record.name)

        df.loc[
            ( df['name'] == last_record.name) & 
            (df['name'] == last_record.name)
        ]

        for i in range(len(df)):
            Customers.objects.create(
                name=df.name[i],
                address=df.address[i],
                checked=df.checked[i],
                description=df.description[i],
                interest=df.interest[i],
                date_of_birth=df.date_of_birth[i],
                email=df.email[i],
                account=df.account[i],
                credit_card=df.credit_card[i]
                
                )

        


     
        return Response(data = {'status': 'Done'})


