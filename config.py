from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key and base URL from environment variables
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")