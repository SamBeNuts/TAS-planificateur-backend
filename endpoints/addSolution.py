import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
from botocore.exceptions import ClientError
from datetime import datetime
from decimal import Decimal
import json

def handler(event, context):
    try:
        Dynamo.put(
            Item={
                "PK": "SOLUTION",
                "SK": datetime.now().isoformat(),
                "JSON": json.loads(event['body'], parse_float=Decimal)
            }
        )
        return Responses._201()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])
