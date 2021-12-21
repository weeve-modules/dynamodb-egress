"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import logging
import boto3
from time import time
from decimal import Decimal
from app.config import APPLICATION
from uuid import uuid4

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
        timestamp = int(time())
        if(type(parsed_data) is list):
            write_batch(parsed_data, timestamp)
        else:
            table.put_item(Item=parse_for_dynamo(parsed_data, timestamp))

        return "", None

    except Exception as e:
        logging.error(e)
        return None, "Unable to perform the module logic"


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
