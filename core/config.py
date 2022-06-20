import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# fixed uri for heroku
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')

EE_SERVICE_ACCOUNT = os.getenv('EE_SERVICE_ACCOUNT')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRIVATE_KEY = os.path.join(BASE_DIR, '.private-key.json')
