import boto3

client = boto3.client('s3')

response = client.list_objects(Bucket='achaubey.club')

for content in response['Contents']:
    obj_dict = client.get_object(Bucket='achaubey.club', Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])
