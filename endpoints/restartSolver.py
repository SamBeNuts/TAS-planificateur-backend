import utils.API_Responses as Responses
import utils.EC2 as EC2 

def handler(event, context):
    EC2.start_instance()
    return Responses._204()
