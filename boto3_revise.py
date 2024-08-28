# code 1
import boto3
mc = boto3.session.Session(profile_name="default")
iam_console = mc.resource('iam')
for each_user in iam_console.users.all():
    print(each_user.name)

# code 2
