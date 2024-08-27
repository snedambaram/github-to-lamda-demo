import json

def lambda_handler(event,context):
    d= {'statusCode': 200,
        'body': json.dumps('Hello world from Git Hub to Lambda 4')
       }
    df = json.loads(d)
    print(df)

  