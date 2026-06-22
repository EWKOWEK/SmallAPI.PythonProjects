import requests
import json
import time
import dotenv
import os
from supabase import create_client, Client

dotenv.load_dotenv()

url: str = os.environ.get("SUPABASE_API_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(url, key)

username = input("Enter the username you want to track: ")

previousData = None

while True:
    response = requests.get(f"https://api.github.com/users/{username}")
    currentData = response.json()

    if previousData != currentData:
        supabase.table("Users").upsert({"username": username,"name": currentData.get("name"),"followers": currentData.get("followers"),"following": currentData.get("following"),"bio": currentData.get("bio", "N/A")}).execute()
        previousData = currentData
    else:
        pass

    time.sleep(10) 
