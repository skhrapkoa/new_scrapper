from typing import Any
import gspread
from google.oauth2.service_account import Credentials
from conf import settings
from gspread import Worksheet


class GoogleSheet:
    def __init__(self, table_url, start_col=1):
        self.table_url = table_url
        self.start_col = start_col
        self.client = self._init_client()

    def _init_client(self):
        creds = Credentials.from_service_account_info(
            self._creds(),
            scopes=[settings.GOOGLE_SCOPES]
        )
        return gspread.authorize(creds)

    @staticmethod
    def _creds() -> dict[str, Any]:
        cred = {
            'type': 'service_account',
            'project_id': settings.GOOGLE_PROJECT_ID,
            'private_key_id': settings.GOOGLE_PRIVATE_KEY_ID,
            "private_key": settings.GOOGLE_PRIVATE_KEY.replace("'", "").replace('"', "").replace("\\n", "\n"),
            'client_email': settings.GOOGLE_CLIENT_EMAIL,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'auth_uri': settings.GOOGLE_AUTH_URI,
            'token_uri': settings.GOOGLE_TOKEN_URI,
            'auth_provider_x509_cert_url': settings.GOOGLE_AUTH_PROVIDER_X509_CERT_URL,
            'client_x509_cert_url': settings.GOOGLE_CLIENT_X509_CERT_URL,
        }
        return cred

    def append_to_column(self, sheet_name: str, row_data: dict[str, list]) -> None:
        wb = self.client.open_by_url(self.table_url)
        ws = wb.worksheet(sheet_name)

        col_values = ws.col_values(self.start_col)
        last_row = len(col_values) + 1

        offset = int(self.start_col)
        for key in row_data:
            self.update_cell(row_data, key, ws, last_row, offset)
            offset += 1

    @staticmethod
    def update_cell(data_dict: dict[str, list], key: str, ws: Worksheet, last_row: int, offset: int):
        for data in data_dict[key]:
            ws.update_cell(last_row, offset, data)
            last_row += 1

    def append_data(self, sheet_name: str, method_name: str, **kwargs):
        method = getattr(self, method_name)
        if not callable(method):
            raise ValueError(f"Method {method_name} not found in GoogleSheet class or it's not callable.")
        method(sheet_name, **kwargs)
