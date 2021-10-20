import os

from gspread.models import Spreadsheet, Worksheet
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
#Create spreadsheet
#dict_keys(['spreadsheetId', 'properties', 'sheets', 'spreadsheetUrl'])
sheets_body = {
  'properties': {
    'title': 'BrickfolioTest',
    'locale': 'en_US',
    'autoRecalc': 'HOUR'
  },
  'sheets': [
    {
      'properties': {
        'title': 'Sheet1'
      }
    }
  ]
}

sheets_file = service.spreadsheets().create(
  body=sheets_body
).execute()

# spreadsheet_id = sheets_file['spreadsheetId']
# worksheet_name = 'Sheet1!'
# cell_range_insert = 'B2'

# with open('Brickfolio.csv', 'r') as file_obj:

#   values = file_obj.read()

#   os.system('clear')
#   print(values)
#   print()
  
#   value_range_body = {
#     'majorDimension': 'ROWS',
#     'values': values
#   }

  # service.spreadsheets().values().update(
  #   spreadsheetId=spreadsheet_id,
  #   valueInputOption='USER_ENTERED',
  #   range=worksheet_name + cell_range_insert,
  #   body=value_range_body
  # ).execute()
