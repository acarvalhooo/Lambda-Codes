# Importação da biblioteca Boto3
import boto3

# Soma do armazenamento total de todos os buckets
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    total_size = 0
    for bucket in s3.buckets.all():
        for obj in bucket.objects.all():
            total_size += obj.size

    total_size_mb = total_size / 2**20
    
# Condição que verifica se total_size_mb é maior ou igual a 50
    if total_size_mb >= 50:
        sns = boto3.client('sns')
        message = f"O seu bucket chegou a {total_size_mb} MB."
        topic_arn = 'xxx' # Altere o xxx para o arn do tópico do SNS
        sns.publish(TopicArn=topic_arn, Message=message)

    return {
        'total_size_mb': total_size_mb
    }
