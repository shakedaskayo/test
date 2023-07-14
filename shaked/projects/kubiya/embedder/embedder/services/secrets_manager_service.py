import boto3
from botocore.exceptions import ClientError

class SecretsManagerService:
    def __init__(self, region_name):
        self.client = boto3.client("secretsmanager", region_name=region_name)

    def get_secret_value(self, secret_name):
        try:
            response = self.client.get_secret_value(SecretId=secret_name)
        except ClientError as e:
            if e.response["Error"]["Code"] == "ResourceNotFoundException":
                print("The requested secret " + secret_name + " was not found")
            elif e.response["Error"]["Code"] == "InvalidRequestException":
                print("The request was invalid due to:", e)
            elif e.response["Error"]["Code"] == "InvalidParameterException":
                print("The request had invalid params:", e)
        else:
            if "SecretString" in response:
                return response["SecretString"]
            else:
                return response["SecretBinary"]

