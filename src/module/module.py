"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
import boto3
from time import time
from decimal import Decimal
from uuid import uuid4
from .params import PARAMS

log = getLogger("module")

__AWS_ACCESS_KEY_ID__ = PARAMS['AWS_ACCESS_KEY_ID']
__AWS_SECRET_ACCESS_KEY__ = PARAMS['AWS_SECRET_ACCESS_KEY']
__REGION__ = PARAMS['REGION']
__TABLE__ = PARAMS['TABLE']

dynamodb = boto3.resource('dynamodb', region_name=__REGION__, aws_access_key_id=__AWS_ACCESS_KEY_ID__, aws_secret_access_key=__AWS_SECRET_ACCESS_KEY__)

table = dynamodb.Table(__TABLE__)

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        # YOUR CODE HERE
        timestamp = int(time())
        if(type(received_data) is list):
            write_batch(received_data, timestamp)
        else:
            table.put_item(Item=parse_for_dynamo(received_data, timestamp))

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"

def convert_to_decimal(data):
    """
    Converts all float values in a dict to Decimal Type
    Args:
        data (JSON Object): data to transform
    Returns:
        data (JSON Object): Transform data
    """
    for key in data:
        if type(data[key]) == float:
            data[key] = Decimal(str(data[key]))
        if type(data[key]) == dict:
            data[key] = convert_to_decimal(data[key])
    return data


def parse_for_dynamo(data, timestamp: int):
    data["id"] = str(uuid4())
    if not "timestamp" in data:
        data['timestamp'] = timestamp
    return convert_to_decimal(data)


def write_batch(dataList: list, timestamp: int):
    """
    Writes batch data to dynamodb
    Args:
        dataList ([JSON Object]): [data to batch write]
        timestamp (timestamp): timestamp
    """
    with table.batch_writer() as batch:
        for data in dataList:
            batch.put_item(Item=parse_for_dynamo(data, timestamp))
