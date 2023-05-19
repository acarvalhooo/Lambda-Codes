# This code was created to use Python 3.9

# Importing boto3 library
import boto3

# Realize the total sum size of all buckets
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    total_size = 0
    for bucket in s3.buckets.all():
        for obj in bucket.objects.all():
            total_size += obj.size

# Convert Bytes to GigaBytes and round to only 3 decimal places
    total_size_gb = round(total_size / 2**30, 3)
    
# Condition that check if total_size_gb is equal to or bigger than 30720 GB
    if total_size_gb >= 30720:
        sns = boto3.client('sns')
        message = f"O seu bucket chegou a {total_size_gb} GB."
        topic_arn = 'xxx' # Change XXX for ARN topic of SNS
        sns.publish(TopicArn=topic_arn, Message=message)

    return {
        'total_size_gb': total_size_gb
    }
