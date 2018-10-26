import os

BASE_URL = 'http://%s/' % os.environ.get('REPIT_INTERNAL_IP', '127.0.0.1:8000')
