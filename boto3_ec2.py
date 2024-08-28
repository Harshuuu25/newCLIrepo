import boto3
m_console = boto3.session.Session(profile_name="default")
ec2_console = m_console.client(service_name="ec2")
# result = ec2_console.describe_instances()
result = ec2_console.describe_instances()['Reservations']
for each_instance in result:
    for value in each_instance['Instances']:
        print(value['InstanceId'])
# print(result)
