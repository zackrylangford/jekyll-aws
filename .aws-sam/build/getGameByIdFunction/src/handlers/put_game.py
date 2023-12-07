import json
import os
import boto3

client = boto3.client('dynamodb')

def putGameHandler(event, context):
    if event["httpMethod"] != "POST":
        raise Exception(f"putItemHandler only accept POST method, you tried: {event.httpMethod}")

    # Get id and name from the body of the request
    body = json.loads(event["body"])
    id = body["id"]
    name = body["name"]

    result = client.put_item(TableName=os.environ["GAMES_TABLE"], Item={"id": {"S": id}, "name": {"S": name}})
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        "body": json.dumps({"message": "Item added successfully"})
    }

    return response