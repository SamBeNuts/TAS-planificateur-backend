import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
from botocore.exceptions import ClientError

def handler(event, context):
    try:
        response = Dynamo.get(
            Key={
                "PK": "PROJECT",
                "SK": "PARAMETERS",
            }
        )
        if 'Item' in response:
            return Responses._200(response['Item'])
        else:
            return Responses._204()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])
