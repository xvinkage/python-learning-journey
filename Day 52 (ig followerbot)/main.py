import os
from dotenv import load_dotenv

load_dotenv()


SIMILAR_ACCOUNT= "rordongamsay"
USERNAME = os.getenv("USERNAME")     # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = os.getenv("PASSWORD") 
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

