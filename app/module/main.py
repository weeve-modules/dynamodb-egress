"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import boto3
import time
from decimal import Decimal
from app.config import APPLICATION

__AWS_ACCESS_KEY_ID__=APPLICATION['AWS_ACCESS_KEY_ID']
__AWS_SECRET_ACCESS_KEY__=APPLICATION['AWS_SECRET_ACCESS_KEY']
__REGION__=APPLICATION['REGION']
__TABLE__=APPLICATION['TABLE']
__OUTPUT_LABEL__=APPLICATION['OUTPUT_LABEL']
__OUTPUT_UNIT__=APPLICATION['OUTPUT_UNIT']

def module_main(parsed_data):
    """
    Implement module logic here. Although this function returns data, remember to implement
    egressing method to external database or another API.

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        dynamodb = boto3.resource('dynamodb', region_name=__REGION__, aws_access_key_id=__AWS_ACCESS_KEY_ID__, aws_secret_access_key=__AWS_SECRET_ACCESS_KEY__)
        table = dynamodb.Table(__TABLE__)
        data_body = {
            'timestamp': int(time.time()),
            __OUTPUT_LABEL__: Decimal(str(parsed_data)),
            'unit': __OUTPUT_UNIT__
        }
        response = table.put_item(Item=data_body)

        return "", None
    except Exception:
        return None, "Unable to perform the module logic"
