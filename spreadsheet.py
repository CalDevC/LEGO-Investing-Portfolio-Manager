from Google import Create_Service
import file_mgr

class Spreadsheet:

    # Returns Google Sheet ID
    def __init__(self):
        CLIENT_SECRET_FILE = 'client_secret.json'
        API_NAME = 'sheets'
        API_VERSION = 'v4'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        # Define spreadsheet body
        sheets_body = {
            'properties': {
                'title': 'myBrickfolio',
                'locale': 'en_US',
                'autoRecalc': 'HOUR'
            }
        }

        # Create spreadsheet  -- dictionary keys: 'spreadsheetId', 'properties', 'sheets', 'spreadsheetUrl'
        sheets_file = self.service.spreadsheets().create(
            body=sheets_body
        ).execute()

        print(sheets_file)

        # Save Spreadsheet
        self.sheet = sheets_file
        self.id = sheets_file['spreadsheetId']
        file_mgr.update_var('CURRENT_BRICKFOLIO', sheets_file)


    def updateSheet(self, start_cell):
        # Read in data from Brickfolio.csv
        with open('Brickfolio.csv', 'r') as file_obj:
            row_list = []

            # Read the values and seperate into rows
            csv_values = file_obj.read()
            csv_rows = csv_values.split('\n')

            for row in csv_rows:
                row_tuple = tuple(row.split(','))
                row_list.append(row_tuple)

        # Assign values
        values = (
            tuple(row_list)
        )

        value_range_body = {
            'majorDimension': 'ROWS',
            'values': values
        }

        # Update sheet
        self.service.spreadsheets().values().update(
            spreadsheetId=self.id,
            valueInputOption='USER_ENTERED',
            range=start_cell,
            body=value_range_body
        ).execute()

    def fetchSheet(self):
        request = self.service.spreadsheets().values().get(
            spreadsheetId=self.id,
            range='Sheet1',
            valueRenderOption='FORMATTED_VALUE'
        )

        response = request.execute()

        print("DATA:\n\n")
        print(response)
