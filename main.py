import json
import traceback
from models.models import secrets_manager
from utils.constants import FIREBASE_KEY_NAME


def main(event, context):
    http_method, body, query_params, path_params, headers = parse_event(event)
    try:
        if path_params:
            return generate_response(path_params)
    except Exception as e:
        traceback.print_exc()
        print(e)
        
def parse_event(event):
    http_method = event.get("httpMethod")
    body = event.get('body')
    if body:
        body = json.loads(body)
    query_params = event.get('queryStringParameters', {})
    path_params = event.get('rawPath', {})
    headers = event.get('headers', {})
    print(event)
    return http_method, body, query_params, path_params, headers
    
def generate_response(path):
    response = {}
    match path:
        case '/dev/get-firebase-key':
            response['statusCode'] = 200
            response['body'] = json.dumps(secrets_manager.get_secret(FIREBASE_KEY_NAME))
        case '/dev/get-other-service-key':
            pass
        case _:
            response['statusCode'] = 500
            response['body'] = json.dumps(f"This request is not yet defined. Path: {path}.")
    return response