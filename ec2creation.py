import boto3
console_aws = boto3.session.Session(profile_name="default")
client_console = console_aws.client(service_name='ec2')
result = client_console.run_instances(
    ImageId='ami-090abff6ae1141d7d',
    InstanceType='t3.micro',
    MaxCount=1,
    MinCount=1,
)