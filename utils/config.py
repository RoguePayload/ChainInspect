import os

# API keys or sensitive information can be stored as environment variables
API_KEY = os.getenv('API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

# Other configuration settings can be defined as constants
DEBUG = True
LOG_FILE = 'app.log'
