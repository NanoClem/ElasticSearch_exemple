import os
from dotenv import load_dotenv


load_dotenv('.env')

CLOUD    = os.getenv('CLOUD')
HOST     = os.getenv('HOST')
PASSWORD = os.getenv('PASSWORD')
DATASET  = os.getenv('DATASET')
INDEX    = os.getenv('INDEX')
