import json

def lambda_handler_hw(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello world from Git Hub to Lambda 1')
    }
