# DynamoDB Egress

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | DynamoDB Egress                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/dynamodb-egress](https://hub.docker.com/r/weevenetwork/dynamodb-egress) |
| authors        | Jakub Grzelak                    |

- [DynamoDB Egress](#dynamodb-egress)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This module is responsible for saving data into the AWS DynamodDB.
For each item being written to a database, this module generates uuid4 ID and a timestamp of receiving that data.
Since AWS DynamodDB does not accept float type data, all floats will be converted to Decimals objects.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                  | Environment Variables | type   | Description                                |
| --------------------- | --------------------- | ------ | ------------------------------------------ |
| AWS Access Key ID     | AWS_ACCESS_KEY_ID     | string | Your AWS Access Key ID                     |
| AWS Secret Access Key | AWS_SECRET_ACCESS_KEY | string | Your AWS Secret Access Key                 |
| Region                | REGION                | string | AWS DynamoDB region, i.e: 'us-east-2'      |
| Table                 | TABLE                 | string | Table name to where you want to write data |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
boto3
uuid
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

* array of JSON body objects, example:

```json
[
    {
        "label-1": 12,
        "label-2": "speed"
    },
    {
        "label-1": 15,
        "label-2": "volume"
    }
]
```

## Output

There is no output for this module, except data written to a database.

