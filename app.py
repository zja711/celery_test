from celery import Celery
"""
celery -A app worker --loglevel=info
"""
cel = Celery('app_name', backend='redis://:myredis-aly@119.23.213.35:6379/0',broker='redis://:myredis-aly@119.23.213.35:6379/0', include=['example.task1'])
