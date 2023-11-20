from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '.', '.env')
load_dotenv(dotenv_path)
from openai import OpenAI

client = OpenAI(
api_key = os.getenv('API_KEY')
)
