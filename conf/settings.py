import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

GOOGLE_PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")
GOOGLE_PRIVATE_KEY_ID = os.getenv("GOOGLE_PRIVATE_KEY_ID")
GOOGLE_PRIVATE_KEY = os.getenv("GOOGLE_PRIVATE_KEY")
GOOGLE_CLIENT_EMAIL = os.getenv("GOOGLE_CLIENT_EMAIL")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_X509_CERT_URL = os.getenv("GOOGLE_CLIENT_X509_CERT_URL")

GOOGLE_AUTH_URI = os.getenv("GOOGLE_AUTH_URI")
GOOGLE_TOKEN_URI = os.getenv("GOOGLE_TOKEN_URI")
GOOGLE_AUTH_PROVIDER_X509_CERT_URL = os.getenv("GOOGLE_AUTH_PROVIDER_X509_CERT_URL")

GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")
GOOGLE_SCOPES = os.getenv("GOOGLE_SCOPES")

SHEET_NAME = os.getenv("SHEET_NAME")
SHEET_START_COL = os.getenv("SHEET_START_COL")
COMPANY_SHEET_NAME = os.getenv("COMPANY_SHEET_NAME")
CONTACT_SHEET_NAME = os.getenv("CONTACT_SHEET_NAME")
GPT_SHEET_NAME = os.getenv("GPT_SHEET_NAME")

COMPANY = "company"

GPT_API_KEY = os.getenv("GPT_API_KEY")
