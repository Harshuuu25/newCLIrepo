import boto3
import urllib.parse
import logging

# Set up logging
logger = logging.getLogger() # gets the root logger
logger.setLevel(logging.INFO) #config the logger to handle messages at the info level

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context): #entry point of ur lambda fn.
    logger.info("Received event: %s", event)
    try:
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = urllib.parse.unquote_plus(record['s3']['object']['key'])
            
            logger.info("Processing file: %s in bucket: %s", key, bucket)
            
            # Define the destination folder and new key
            destination_folder = 'processed/'
            new_key = destination_folder + key.split('/')[-1]

            # Copy the object to the new folder
            s3.copy_object(
                Bucket=bucket,
                CopySource={'Bucket': bucket, 'Key': key},
                Key=new_key
            )
            logger.info("Copied file to: %s", new_key)

            # Delete the original object
            s3.delete_object(Bucket=bucket, Key=key)
            logger.info("Deleted original file: %s", key)

            # Send SNS notification
            sns.publish(
                TopicArn='arn:aws:sns:eu-north-1:315468868369:lambdanotification',
                Message=f'File {key} moved to {new_key} in bucket {bucket}.',
                Subject='S3 Object Moved'
            )
            logger.info("Sent SNS notification for file: %s", new_key)
    except Exception as e:
        logger.error("Error processing file: %s", key)
        logger.error(e)

    return {
        'statusCode': 200,
        'body': 'Success'
    }
