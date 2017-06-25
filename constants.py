import json
from decouple import config as decouple

CLIENT_ID = json.loads(open('client_secret.json', 'r').read())['web']['client_id']
GOOGLE_API_KEY = decouple('GOOGLE_API_KEY')
