import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = join(dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

LOTTO_URL = "https://gateway.wma.olg.ca/feeds/past-winning-numbers?"
OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
LOTTO_X_CLIENT_KEY = os.getenv("X_CLIENT_ID")