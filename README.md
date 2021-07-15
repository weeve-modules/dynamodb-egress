# DynamoDB Egress

|              |                                                                |
| ------------ | -------------------------------------------------------------- |
| name         | DynamoDB Egress                                                |
| version      | v0.0.1                                                         |
| docker image | [weevenetwork/weeve-egress-dynamodb](https://linktodockerhub/) |
| authors      | Jakub Grzelak                                                  |


- [DynamoDB Egress](#dynamodb-egress)
  - [Description](#description)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Examples](#examples)
    - [Input](#input)
    - [Output](#output)



## Description

This module is responsible for saving data into the AWS DynamodDB.
For each item being written to a database, this module generates uuid4 ID and a timestamp of receiving that data.
Since AWS DynamodDB does not accept float type data, all floats will be converted to Decimals objects.

## Features

* Flask ReST client
* Request - sends HTTP Request to the next module
* boto3

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                  | Environment Variables | type   | Description                                |
| --------------------- | --------------------- | ------ | ------------------------------------------ |
| AWS Access Key ID     | AWS_ACCESS_KEY_ID     | string | Your AWS Access Key ID                     |
| AWS Secret Access Key | AWS_SECRET_ACCESS_KEY | string | Your AWS Secret Access Key                 |
| Region                | REGION                | string | AWS DynamoDB region, i.e: 'us-east-2'      |
| Table                 | TABLE                 | string | Table name to where you want to write data |

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| EGRESS_API_HOST       | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                     |


## Dependencies

```txt
Flask==1.1.1
python-dotenv
boto3
uuid
```

## Examples

### Input

```json
// Single item
{
  "temperature": 10
}
// Batch of data
[
  {
  "temperature": 10.01
  },
  {
  "temperature": 12.23
  }
]
```
### Output

There is no output for this module, except data written to a database.