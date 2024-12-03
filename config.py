from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key and base URL from environment variables
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

# Get database and other configurations from the .env file
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")