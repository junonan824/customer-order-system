import boto3


class SQSQueue:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.sqs = boto3.client('sqs', region_name='us-west-2')  # Specify your region here

    def send_message(self, message_body):
        queue_url = self.sqs.get_queue_url(QueueName=self.queue_name)['QueueUrl']
        response = self.sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        return response