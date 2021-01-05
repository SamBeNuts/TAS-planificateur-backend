import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
import utils.EC2 as EC2 
from botocore.exceptions import ClientError

def handler(event, context):
    try:
        Dynamo.delete(
            Key={
                "PK": "PROJ#" + event['pathParameters']['date'],
                "SK": "CONS#" + event['pathParameters']['code'],
            }
        )
        EC2.start_instance()
        return Responses._204()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])
