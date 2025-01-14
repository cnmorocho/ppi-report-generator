import os
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

from services.ppi_service import PpiCredentials, PpiService

BASE_URL = os.getenv("BASE_URL", "")
AUTHORIZED_CLIENT = os.getenv("AUTHORIZED_CLIENT", "")
CLIENT_KEY = os.getenv("CLIENT_KEY", "")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY", "")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY", "")
SHEET_ID = os.getenv("SHEET_ID", "")

def get_google_sheet(credentials_path, sheet_id, sheet_index):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]

    credentials = Credentials.from_service_account_file(credentials_path, scopes=scopes)
    client = gspread.authorize(credentials)

    sheet = client.open_by_key(sheet_id)

    return sheet.get_worksheet(sheet_index)


def main():

    ppi_credentials = PpiCredentials(
        authorized_client=AUTHORIZED_CLIENT,
        client_key=CLIENT_KEY,
        public_key=PUBLIC_KEY,
        private_key=PRIVATE_KEY,
    )
    ppi_service = PpiService(BASE_URL, ppi_credentials)
    gruped_instruments = ppi_service.get_instruments()

    sheet = get_google_sheet("credentials.json", SHEET_ID, 0)

    for instrument_types in gruped_instruments:
        for instrument in instrument_types["instruments"]:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.append_row(values=[now, instrument_types["name"], instrument["ticker"], instrument["description"], instrument["currency"], instrument["price"], instrument["quantity"], instrument["amount"]], value_input_option="USER_ENTERED")

if __name__ == "__main__":
    main()
