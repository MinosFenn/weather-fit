import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
    LOCATION = 'geneva,ch' 
 # Hardcoded location
