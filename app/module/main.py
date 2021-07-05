"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import logging
import boto3
import time
from decimal import Decimal
from app.config import APPLICATION

__AWS_ACCESS_KEY_ID__ = APPLICATION['AWS_ACCESS_KEY_ID']
__AWS_SECRET_ACCESS_KEY__ = APPLICATION['AWS_SECRET_ACCESS_KEY']
__REGION__ = APPLICATION['REGION']
__TABLE__ = APPLICATION['TABLE']

dynamodb = boto3.resource('dynamodb', region_name=__REGION__,
                          aws_access_key_id=__AWS_ACCESS_KEY_ID__, aws_secret_access_key=__AWS_SECRET_ACCESS_KEY__)

table = dynamodb.Table(__TABLE__)


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

        # data_body = {
        #     'timestamp': int(time.time()),
        #     __OUTPUT_LABEL__: str(parsed_data),
        #     'unit': __OUTPUT_UNIT__
        # }

        logging.info(parsed_data)
        parsed_data['timestamp'] = int(time.time())
        logging.info(parsed_data)

        table.put_item(Item=parsed_data)

        return "", None
    except Exception as e:
        logging.error(e)
        return None, "Unable to perform the module logic"
