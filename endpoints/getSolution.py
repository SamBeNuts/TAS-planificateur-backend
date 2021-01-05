import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
from botocore.exceptions import ClientError

def handler(event, context):
    try:
        response = Dynamo.query(
            KeyConditionExpression="PK=:PK AND begins_with(SK, :SK)",
            ExpressionAttributeValues={
                ":PK": "PROJ#" + event['pathParameters']['date'],
                ":SK": "SOL",
            },
            Limit=1,
            ScanIndexForward=False
        )
        if 'Items' in response and len(response['Items']) > 0:
            return Responses._200(response['Items'])
        else:
            return Responses._204()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])
