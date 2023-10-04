import boto3

ecr_client = boto3.client('ecr', region_name='ca-central-1')

repository_name = "my_demo-python"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)

#os.environ['AWS_ACCESS_KEY_ID'] = 'your-access-key-id'
#os.environ['AWS_SECRET_ACCESS_KEY'] = 'your-secret-access-key'
#os.environ['AWS_DEFAULT_REGION'] = 'ca-central-1'  # Replace with your desired region

#aws_access_key_id='AKIATQX65TXA3WDXYFZY', aws_secret_access_key='3QiHTiRlPOSzaxVgElVJUnd8RSM452SJybh37YhD'