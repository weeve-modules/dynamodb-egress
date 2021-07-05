"""
All logic related to the module's incoming data validation
Mostly this file requires changes
"""

from decimal import Decimal
from app.config import APPLICATION


def data_validation(data):
    """Validates the incoming JSON data

    Args:
        data ([JSON Object]): [This is the request body in json format]

    Returns:
        [str, str]: [data, error]
    """
    try:
        return convert_to_decimal(data), None
    except Exception:
        return None, 'Invalid INPUT_LABEL'


def convert_to_decimal(data):
    for key in data:
        if type(data[key]) == float:
            data[key] = Decimal(str(data[key]))
        if type(data[key]) == dict:
            data[key] = convert_to_decimal(data[key])
    return data
