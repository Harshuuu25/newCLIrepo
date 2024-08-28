import boto3
from pprint import pprint
m_console = boto3.session.Session(profile_name="default") 

iam_console = m_console.client(service_name="iam") 
result = iam_console.list_users()
# print(result)
# pprint(result['Users'])
# pprint(result)
for each_user in result['Users']:
    print(each_user['UserName'])
# in above 2 lines we are working with client so we will get our result in dictionary
#  looping it because of two many users
