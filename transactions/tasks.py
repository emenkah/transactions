from celery import shared_task

import pandas as pd
import os
from .models import Transactions
from .utility import date_converter, age_computer, credit_card_number_match



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
        '''
            code to read heavy file as binary or line of line or loading up data in buffers here
        '''

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


        """
            Credit Card pattern Checker
            When pattern is ag
        """
        pattern ="[45][0-9]{12}"
        card_pass = credit_card_number_match(df.credit_card[i]["number"], pattern=pattern)
        

        if (card_pass) and (age == None or (age > 18 and age < 65)):
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
