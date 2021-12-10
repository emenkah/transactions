from celery import shared_task

import pandas as pd
import sys, os
from .models import Transactions
from .utility import date_converter, age_computer



@shared_task
def transactions_read(path):
    '''
        Read file using path
    '''

    name, extension = os.path.splitext(path)

    try:
        if extension == '.json':
            df = pd.read_json(path)
            df['date_of_birth'] = df['date_of_birth'].transform(date_converter)
        elif extension == '.csv':
            df = pd.read_csv(path, converters= {'date_of_birth' : date_converter})
        elif extension == 'xml':
            df = pd.read_xml(path)


    except MemoryError as e: 
        pass

    '''
        Apply data transformation to obtain dates in uniform fashion
    '''
    

    last_record = None
    last_record = Transactions.objects.all().order_by('position').last()

    lowerbound = 0
    if last_record: 
        lowerbound = last_record.position

        if lowerbound > len(df) :
            return "Check Records well, Starting point %s is greater than %s of records to be read"%(lowerbound, len(df)) 
        if lowerbound == len(df) :
            return "All Records already read in"
    
    record_counter = lowerbound

    for i in range(lowerbound, len(df)):
        record_counter += 1
       
        '''
            ONLY process records for which the subject's age is between 18 and 65 (or is unknown). 
        '''
        age = age_computer(df.date_of_birth[i])
        if age == None or (age > 18 and age < 65):
            Transactions.objects.create(
                name=df.name[i],
                address=df.address[i],
                checked=df.checked[i],
                description=df.description[i],
                interest=df.interest[i],
                date_of_birth=df.date_of_birth[i],
                email=df.email[i],
                account=df.account[i],
                credit_card=df.credit_card[i],
                position=record_counter
                
                )
    

    return record_counter
