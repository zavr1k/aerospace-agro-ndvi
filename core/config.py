import os

from dotenv import load_dotenv

from core.credentials import create_private_key

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_URL = os.getenv('DATABASE_URL')
# fixed uri for heroku
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')

# --- Google Service Account credentials ---
EE_PROJECT_ID = os.getenv('EE_PROJECT_ID')
EE_PRIVATE_KEY_ID = os.getenv('EE_PRIVATE_KEY_ID')
EE_PRIVATE_KEY = os.getenv('EE_PRIVATE_KEY')
EE_CLIENT_EMAIL = os.getenv('EE_CLIENT_EMAIL')
EE_CLIENT_ID = os.getenv('EE_CLIENT_ID')

PRIVATE_KEY = os.path.join(BASE_DIR, '.private-key.json')
if not os.path.exists(PRIVATE_KEY):
    create_private_key()
# --- end ---
