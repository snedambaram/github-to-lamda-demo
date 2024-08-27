import json

def lambda_handler(event,context):
     x = {
        "name": "Sreeni",
        "message": "Hello World from Github",
        "city": "Atlanta"
        }

        # convert into JSON:
     y = json.dumps(x)

        # the result is a JSON string:
     print(y)

  