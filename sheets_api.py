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

#Create Google Sheet
sheets_file = service.spreadsheets().create(
  body=sheets_body
).execute()

#Sheet info
spreadsheet_id = sheets_file['spreadsheetId']
worksheet_name = 'Sheet1!'
cell_range_insert = 'B2'

#Read in data from Brickfolio.csv
with open('Brickfolio.csv', 'r') as file_obj:
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
service.spreadsheets().values().update(
  spreadsheetId=spreadsheet_id,
  valueInputOption='USER_ENTERED',
  range=worksheet_name + cell_range_insert,
  body=value_range_body
).execute()
