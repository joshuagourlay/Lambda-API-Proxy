import requests

def make_api_request(url, headers, data):
    response = requests.post(url, headers=headers, data=data)
    return response.json()