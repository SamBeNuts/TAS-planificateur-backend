import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
from botocore.exceptions import ClientError

def handler(event, context):
    try:
        Dynamo.put(Item={
            'PK': 'PROJECT',
            'SK': event['pathParameters']['date']
        })
        return Responses._201()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])
