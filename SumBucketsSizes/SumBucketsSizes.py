# Importing boto3 library
import boto3

# Realize the total sum size of all buckets
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    total_size = 0
    for bucket in s3.buckets.all():
        for obj in bucket.objects.all():
            total_size += obj.size

# Convert bytes to gigabytes and round to only 3 decimal places
    total_size_gb = round(total_size / 2**30, 3)

    return {
        'total_size_gb': total_size_gb
    }
