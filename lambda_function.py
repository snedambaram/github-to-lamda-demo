import pandas as pd
import json

def lambda_handler(event,context):
    d= {'statusCode': 200,
        'body': json.dumps('Hello world from Git Hub to Lambda 3')
       }
    df = pd.DataFrame(data=d)
    print(df)

    print('Done x1.16')