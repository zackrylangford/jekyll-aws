import json
import os
import boto3

client = boto3.client('dynamodb')

def deleteGameHandler(event, context):
    if event["httpMethod"] != "DELETE":
        raise Exception(f"deleteByIdHandler only accepts DELETE method, you tried: {event['httpMethod']}")

    id = event["pathParameters"]["id"]
    client.delete_item(TableName=os.environ["GAMES_TABLE"], Key={"id": {"S": id}})
    
    response = {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        "body": json.dumps({"message": "Game deleted successfully"})
    }


    return response
