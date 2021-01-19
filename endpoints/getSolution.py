import utils.API_Responses as Responses
import utils.Dynamo as Dynamo
from botocore.exceptions import ClientError
import pandas as pd
import plotly.figure_factory as ff

def handler(event, context):
    try:
        response = Dynamo.query(
            KeyConditionExpression="PK=:PK",
            ExpressionAttributeValues={
                ":PK": "SOLUTION",
            },
            Limit=1,
            ScanIndexForward=False
        )
        if 'Items' in response and len(response['Items']) > 0 and 'JSON' in response['Items'][0]:
            json = response['Items'][0]['JSON']
            if event['queryStringParameters'] is not None and event['queryStringParameters']['gantt'] != '1':
                return Responses._200(json)
            return {
                'headers': {
                    'Content-Type': 'text/html',
                    'Access-Control-Allow-Methods': '*',
                    'Access-Control-Allow-Origin': '*',
                },
                'statusCode': 200,
                'body': create_html_gantt_from_json(json),
            }
        else:
            return Responses._204()
    except ClientError as e:
        return Responses._CustomResponse(e.response['Error']['Message'], e.response['ResponseMetadata']['HTTPStatusCode'])

def create_html_gantt_from_json(json):
    solution = pd.DataFrame(json)
    solution = solution[solution.IsPresent == True]
    fig = ff.create_gantt(solution, index_col='Part', show_colorbar=True, group_tasks=True)
    return fig.to_html(full_html=False)