import os

from gspread.models import Spreadsheet, Worksheet
from Google import Create_Service

class Spreadsheet:
  
  # Returns Google Sheet ID
  def __init__(self):
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    #Define spreadsheet body
    sheets_body = {
      'properties': {
        'title': 'BrickfolioTest',
        'locale': 'en_US',
        'autoRecalc': 'HOUR'
      }
    }

    #Create spreadsheet  -- dictionary keys: 'spreadsheetId', 'properties', 'sheets', 'spreadsheetUrl'
    sheets_file = self.service.spreadsheets().create(
      body=sheets_body
    ).execute()

    #Return Spreadsheet id
    self.spreadsheet_id = sheets_file['spreadsheetId']

  def updateSheet(self, start_cell):

    #Read in data from Brickfolio.csv
    with open('myBrickfolio.csv', 'r') as file_obj:
      row_list = []

      #Read the values and seperate into rows
      csv_values = file_obj.read()
      csv_rows = csv_values.split('\n')
      
      for row in csv_rows:
        row_tuple = tuple(row.split(','))
        row_list.append(row_tuple)

    #Assign values
    values = (
      tuple(row_list)
    )

    value_range_body = {
      'majorDimension': 'ROWS',
      'values': values
    }

    #Update sheet
    self.service.spreadsheets().values().update(
      spreadsheetId=self.spreadsheet_id,
      valueInputOption='USER_ENTERED',
      range=start_cell,
      body=value_range_body
    ).execute()

