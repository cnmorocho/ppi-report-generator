import requests

class PpiCredentials:
    def __init__(self, authorized_client, client_key, public_key, private_key, account_number=None):
        self.authorized_client = authorized_client
        self.client_key = client_key
        self.public_key = public_key
        self.private_key = private_key
        self.account_number = account_number

class PpiService:
    def __init__(self, base_url, credentials):
        if not isinstance(credentials, PpiCredentials):
            raise ValueError("credentials must be an instance of PpiCredentials")
        self.base_url = base_url
        self.credentials = credentials
        self.token_url = f"{self.base_url}/api/1.0/Account/LoginApi"
        self.account_url = f"{self.base_url}api/1.0/Account/Accounts"
        self.balance_url = f"{self.base_url}api/1.0/Account/BalancesAndPositions?accountNumber="

    def _get_token(self):
        headers = {
            "AuthorizedClient": self.credentials.authorized_client,
            "ClientKey": self.credentials.client_key,
            "ApiKey": self.credentials.public_key,
            "Content-Type": "application/json",
            "ApiSecret": self.credentials.private_key
        }
        response = requests.post(self.token_url, headers=headers)
        response.raise_for_status()
        return response.json()["accessToken"]

    def _get_account_number(self, token):
        headers = {
            "AuthorizedClient": self.credentials.authorized_client,
            "ClientKey": self.credentials.client_key,
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(self.account_url, headers=headers)
        response.raise_for_status()
        return response.json()[0]["accountNumber"]


    def get_instruments(self):
        token = self._get_token()
        account_number = self._get_account_number(token)

        headers = {
            "AuthorizedClient": self.credentials.authorized_client,
            "ClientKey": self.credentials.client_key,
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(f"{self.balance_url}{account_number}", headers=headers)
        response.raise_for_status()
        return response.json()["groupedInstruments"]
