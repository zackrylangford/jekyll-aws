import json
import os
import boto3

client = boto3.client('dynamodb')

def getAllGamesHandler(event, context):
    if event["httpMethod"] != "GET":
        raise Exception(f"getAllItems only accept GET method, you tried: {event.httpMethod}")

    data = client.scan(TableName=os.environ["GAMES_TABLE"])
    items = data["Items"]
    response = {
        "statusCode": 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
        },
        "body": json.dumps(items)
    }

    return response
