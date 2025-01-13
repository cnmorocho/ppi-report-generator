import os
from services.ppi_service import PpiCredentials, PpiService

BASE_URL = os.environ.get("BASE_URL") or ""
AUTHORIZED_CLIENT = os.environ.get("AUTHORIZED_CLIENT") or ""
CLIENT_KEY = os.environ.get("CLIENT_KEY") or ""
PUBLIC_KEY = os.environ.get("PUBLIC_KEY") or ""
PRIVATE_KEY = os.environ.get("PRIVATE_KEY") or ""


def main():
    ppi_credentials = PpiCredentials(
        authorized_client=AUTHORIZED_CLIENT,
        client_key=CLIENT_KEY,
        public_key=PUBLIC_KEY,
        private_key=PRIVATE_KEY,
    )
    ppi_service = PpiService(BASE_URL, ppi_credentials)
    print(ppi_service.get_balance())

if __name__ == "__main__":
    main()
