import json
from main import main

def lambda_handler(event, context):
    response = main(event, context)
    return response
    
