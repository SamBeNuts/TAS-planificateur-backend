import boto3
import os

dynamodb = None

if not dynamodb:
    if os.getenv('IS_OFFLINE'):
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000").Table('ProjIntegrateur')
    else:
        dynamodb = boto3.resource('dynamodb').Table('ProjIntegrateur')

get = dynamodb.get_item

put = dynamodb.put_item

update = dynamodb.update_item

delete = dynamodb.delete_item

query = dynamodb.query
