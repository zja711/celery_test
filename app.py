from celery import Celery
from config import *
"""
celery -A app worker --loglevel=info
"""
cel = Celery('app_name', **REDIS_CONFIG)
