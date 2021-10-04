import os

from dotenv import load_dotenv
from kombu.utils.url import safequote


load_dotenv()


CELERY_BROKER_TRANSPORT_OPTIONS = {
    'region': os.getenv('AWS_REGION'),
    'predefined_queues': {
        'default': {
            'url': os.getenv('SQS_URL'),
        }
    }
}

aws_access_key = safequote(os.getenv('AWS_ACCESS_KEY_ID'))
aws_secret_key = safequote(os.getenv('AWS_SECRET_ACCESS_KEY'))

broker_url = "sqs://{aws_access_key}:{aws_secret_key}@".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)
result_backend = 'rpc://'
enable_utc = True
