import re
def normalize_phone (phone_number):
    cleaned_number = re.sub(r'[^0-9+]','',phone_number)
    
    if cleaned_number.startswith ('0'):
         cleaned_number = '+38' + cleaned_number.lstrip ('0')
    elif cleaned_number.startswith ('380'):
        cleaned_number = '+' + cleaned_number
    elif not cleaned_number.startswith ('+'):
        cleaned_number = '+38' + cleaned_number
    return cleaned_number

