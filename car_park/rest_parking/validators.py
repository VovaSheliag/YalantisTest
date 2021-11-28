from django.core.exceptions import ValidationError
import re


def plate_number_validator(value):
    to_find = re.findall(r'\b[A-Z]{2} \d\d\d\d [A-Z]{2}\b', value)
    if len(to_find) == 0:
        raise ValidationError(f'{value} is a wrong plate number')
