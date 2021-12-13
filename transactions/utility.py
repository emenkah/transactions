import re
from datetime import datetime, date


def credit_card_number_match(card_number, pattern):

    '''Regex to perform a pattern to filter out certain records based on credit card numbers
    
    Arguments
	---------
		pattern (string):  search or sequence pattern
		card_number (string): Credit card number

	Returns
	-------
		bool: True/False
        
    '''

    
    if re.search(pattern, card_number):
        return True
    else:
        return False


def date_converter(cell):
    
    '''
        Utility function to transform/reformat date for uniformity.
        Dates with timezone indcation, '2003-10-31T13:31:56+00:00', stay the same.
        Dates with no timezone but time component separated with space, '1955-12-05 00:00:00'
        gets 'T' added and normalized to GMT timezone.
        Dates with no time components, '12/09/1970', get reformated with hypens, time of 00:000:00 added
        to it with timezone of GMT: -> 1970-09-12T00:00:00+00:00
    '''
    
    date_of_birth = cell
    if cell != None and cell.find("/") != -1: 
        date_in_parts = cell.split('/')
        date_new_format = date_in_parts[2] + '-' + date_in_parts[1] + '-' + date_in_parts[0] + 'T00:00:00+00:00'
        date_of_birth = date_new_format
    elif cell != None and cell.find(" ") != -1:
        date_in_parts = cell.split(' ')
        date_new_format = date_in_parts[0] + 'T' + date_in_parts[1] + '+00:00'
        date_of_birth = date_new_format

    return date_of_birth


def age_computer(date_of_birth):
    '''Utility function to compute age from date of birth.

	Arguments
	---------
		date_of_birth (string): date of birth in this form 1970-09-12T00:00:00+00:00

	Returns
	-------
		float: age in days/365
    Raises
	------
		AttributeError: if date is not in any meaningful format 
	    
    '''
    try:
        if date_of_birth != None and ( date_of_birth.find(" ") != -1 or date_of_birth.find("T") !=-1):
            date_component = re.split(' | |T', date_of_birth)
            date_obj = datetime.strptime(date_component[0], "%Y-%m-%d")
        elif date_of_birth == None:
            return None
        else: 
            date_obj = datetime.strptime(date_of_birth, "%Y-%m-%d")
    except AttributeError as e:

        return e
    
    age_delta = date.today() - date_obj.date()
    age = age_delta.days/365

    return age
