# commands for accessing the instance
cd downloads
chmod 0400 tesing.pem
ssh ec2-user @<"ip address"> -i tesing.pem
# command for super user 
sudo su 

# commands related to httpd
yum install httpd
sudo systemctl start httpd
sudo systemctl enable httpd
# !/bin/bash
# install the agent on linux 2
sudo yum install amazon-cloudwatch-agent

# run the wizard
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard 

# create some missing files
sudo mkdir -p /usr/share/collected
sudo touch /usr/share/collected/type.db

# options 
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2
-c ssm: AmazonCloudWatch-linux -s

# alam --> cloud watch
aws cloudwatch set-alarm-state --alarm-name -->("our alarm name")<--  --state-value ALARM --state-reason"testing recovery action"
aws cloudwatch set-alarm-state --alarm-name awsec2-i-0b5ca1f3bfe07929a-GreaterThanOrEqualToThreshold-StatusCheckFailed_System --state-value ALARM --state-reason "testing recovery action"


# cli commands for aws cli
aws configure
aws help
aws ec2 help # u can name any instance instead of ec2 here for accessing all the commands.
aws ec2 describe-instances --region eu-north-1 # it will decribe ur pre built instance details.
aws ec2 run-instances helpaws ec2 run-instances --image-id=ami-02af70169146bbdd3 --instance-type=t3.micro --region=eu-north-1
aws s3 ls
aws s3 cp assignment.jpeg s3://buckve/ #samplefromec2.txt
aws s3 cp s3://buckve/samplefromec2.txt assignmentfroms3.jpeg # downloading the file.
[--image-id <value>]
[--instance-type <value>]

# boto3 imp concepts & installation

pip install boto3 # for installing boto3
step1: python
step2: import boto3
step3: m_console = boto3.session.Session(profile_name="default")   #session(code) 
step4: dir(m_console)     #dir(print krana)
step5: print(m_console.get_available_resources())
#To get what are the available resources and which are accessable by a resource object

session
resoruce
client
meta
collectors
waiters 
paginators


# 