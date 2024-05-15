from os import getenv
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Database configuration
DB_NAME = getenv()
DB_PASSWORD = getenv()

# API configuration
API_KEY = ''

# Other configurations

