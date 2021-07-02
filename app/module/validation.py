"""
All logic related to the module's incoming data validation
Mostly this file requires changes
"""

from app.config import APPLICATION


def data_validation(data):
    """Validates the incoming JSON data

    Args:
        data ([JSON Object]): [This is the request body in json format]

    Returns:
        [str, str]: [data, error]
    """
    try:
        return float(data[APPLICATION['INPUT_LABEL']]), None
    except Exception:
        return None, 'Invalid INPUT_LABEL'
