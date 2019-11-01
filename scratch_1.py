import boto3
from pprint import pprint
client = boto3.client('ec2')
response = client.describe_instances()
for i in response['Reservations']:
    for k in i['']
    pprint(i)