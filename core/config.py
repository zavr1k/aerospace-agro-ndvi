import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
EE_SERVICE_ACCOUNT = os.getenv('EE_SERVICE_ACCOUNT')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRIVATE_KEY = os.path.join(BASE_DIR, '.private-key.json')
