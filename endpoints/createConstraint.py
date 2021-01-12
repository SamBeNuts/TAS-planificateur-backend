import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
import utils.EC2 as EC2 
from botocore.exceptions import ClientError
from datetime import datetime

def handler(event, context):
    item = {
            "PK": "CONSTRAINT",
            "SK": datetime.now().isoformat(),
            "modifiedAt": datetime.now().isoformat()
        }
    for key, value in event['queryStringParameters'].items():
        if key != 'force':
            item[key] = value
    try:
        Dynamo.put(Item=item)
        EC2.start_instance(event['queryStringParameters'])
        return Responses._201()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])
