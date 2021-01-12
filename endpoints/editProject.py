import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
import utils.EC2 as EC2 
from botocore.exceptions import ClientError
from datetime import datetime

def handler(event, context):
    parameters = event["pathParameters"]
    try:
        Dynamo.put(Item={
            "PK": "PROJECT",
            "SK": "PARAMETERS",
            "MECA1": parameters["meca1"],
            "QUAL1": parameters["qual1"],
            "MECA2": parameters["meca2"],
            "QUAL2": parameters["qual2"],
            "DURATION": parameters["duration"],
            "METHOD": 1,
            "modifiedAt": datetime.now().isoformat()
        })
        EC2.start_instance(event['queryStringParameters'])
        return Responses._204()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])
