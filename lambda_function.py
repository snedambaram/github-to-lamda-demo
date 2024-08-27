import pandas as pd
import json

def lambda_handler(event,context):
    d= {'statusCode': 200,
        'body': json.dumps('Hello world from Git Hub to Lambda 3')
       }
    df = pd.DataFrame(data=d)
    print(df)

    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)