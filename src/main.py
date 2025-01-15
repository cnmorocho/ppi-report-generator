import os
from datetime import datetime
from services.ppi_service import PpiCredentials, PpiService
from services.google_sheet_service import GoogleSheetService
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "")
AUTHORIZED_CLIENT = os.getenv("AUTHORIZED_CLIENT", "")
CLIENT_KEY = os.getenv("CLIENT_KEY", "")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY", "")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY", "")
SHEET_ID = os.getenv("SHEET_ID", "")
WORKSHEET_INDEX = 0
GOOGLE_CREDENTIALS_PATH = "credentials.json"

def main():
    ppi_credentials = PpiCredentials(
        authorized_client=AUTHORIZED_CLIENT,
        client_key=CLIENT_KEY,
        public_key=PUBLIC_KEY,
        private_key=PRIVATE_KEY,
    )
    ppi_service = PpiService(BASE_URL, ppi_credentials)
    gruped_instruments = ppi_service.get_instruments()

    google_sheet_service = GoogleSheetService(GOOGLE_CREDENTIALS_PATH, SHEET_ID, WORKSHEET_INDEX)
    worksheet = google_sheet_service.get_worksheet()

    for instrument_types in gruped_instruments:
        for instrument in instrument_types["instruments"]:
            today = datetime.now().strftime("%Y-%m-%d")
            worksheet.append_row(values=[today, instrument_types["name"], instrument["ticker"], instrument["description"], instrument["currency"], instrument["price"], instrument["quantity"], instrument["amount"]], value_input_option="USER_ENTERED")

if __name__ == "__main__":
    main()
