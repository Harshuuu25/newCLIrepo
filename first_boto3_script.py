import boto3

aws_management_console = boto3.session.Session(profile_name="default") 
#  in above line we need to provide the username that we configured mainly known as default.
iam_console = aws_management_console.resource('iam')
iam_console_client = aws_management_console.client('iam')

#  IAM users list with resource object:
for each_user in iam_console.users.all():
    print(each_user.name)
  
# IAM users list with client object:
for each in iam_console_client.list_users()['Users']:
   print(each['UserName']) 