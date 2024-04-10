import boto3
import os
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Secrets(metaclass=Singleton):
    def __init__(self):
        self._secrets_data = {}

    def load_secrets(self):
        if not self._secrets_data:
            client = boto3.client('secretsmanager')
            secret_name = "prod/running-secrets"
            response = client.get_secret_value(SecretId=os.environ.get("secrets_arn"))
            self._secrets_data = json.loads(response['SecretString'])

    def get_secret(self, key):
        return self._secrets_data.get(key)
   
    
secrets_manager = Secrets()
secrets_manager.load_secrets()