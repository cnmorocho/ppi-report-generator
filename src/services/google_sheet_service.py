import gspread

from google.oauth2.service_account import Credentials

class GoogleSheetService:
    def __init__(self, credentials_path, sheet_id, worksheet_index):
        self.credentials_path = credentials_path
        self.sheet_id = sheet_id
        self.worksheet_index = worksheet_index
        self.scopes = [
            "https://www.googleapis.com/auth/spreadsheets"
        ]
        self.credentials = Credentials.from_service_account_file(self.credentials_path, scopes=self.scopes)


    def get_worksheet(self):
        try:
            client = gspread.authorize(self.credentials)
            sheet = client.open_by_key(self.sheet_id)
            return sheet.get_worksheet(self.worksheet_index)
        except Exception as e:
            print("Error getting google worksheet: ", e)
            return None
