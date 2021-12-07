

def date_converter(cell):

    '''
        Utility function to reformat date for uniformity.
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