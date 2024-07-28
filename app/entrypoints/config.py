import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///orders.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQS_QUEUE_NAME = os.getenv('SQS_QUEUE_NAME', 'order-queue')
    AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')  # Default to 'us-west-2'