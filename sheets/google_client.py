import json
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv


# Load environment variables from .envrc file or .env file
load_dotenv()

scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds_json = os.getenv("GOOGLE_API_KEY")
sheets_id = os.getenv("GOOGLE_SHEET_ID")
creds_dict = json.loads(creds_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open_by_key(sheets_id)

emails_worksheet = sheet.worksheet("emails")
user_input_activity = sheet.worksheet("user_input")
