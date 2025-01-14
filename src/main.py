import os
from services.ppi_service import PpiCredentials, PpiService

BASE_URL = os.getenv("BASE_URL", "")
AUTHORIZED_CLIENT = os.getenv("AUTHORIZED_CLIENT", "")
CLIENT_KEY = os.getenv("CLIENT_KEY", "")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY", "")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY", "")

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
