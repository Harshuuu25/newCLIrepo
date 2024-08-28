import boto3
console_aws = boto3.session.Session(profile_name="default")
client_console = console_aws.client('ec2')
response = client_console.terminate_instances(
    InstanceIds=['i-07e1dc36feadc6f62']
)