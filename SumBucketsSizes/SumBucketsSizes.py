# Importação da biblioteca Boto3
import boto3

# Soma do armazenamento total de todos os buckets
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    total_size = 0
    for bucket in s3.buckets.all():
        for obj in bucket.objects.all():
            total_size += obj.size

# Converte Bytes para GigaBytes e arredona para apenas 3 casas decimais após a vírgula
    total_size_gb = round(total_size / 2**30, 3)
    
# Condição que verifica se total_size_gb é maior ou igual a 30720 GB
    if total_size_gb >= 30720:
        sns = boto3.client('sns')
        message = f"O seu bucket chegou a {total_size_gb} GB."
        topic_arn = 'xxx' # Troque o XXX pelo ARN do tópico desejado do SNS
        sns.publish(TopicArn=topic_arn, Message=message)

    return {
        'total_size_gb': total_size_gb
    }
