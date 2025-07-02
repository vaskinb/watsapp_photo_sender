# coding: utf-8
import os

# -----------------------------------------------------------------------------
# --- Dotenv ---
# -----------------------------------------------------------------------------
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------------------------------------------------
# --- WhatsApp config ---
# -----------------------------------------------------------------------------
VERIFY_TOKEN: str = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID: str = os.getenv("PHONE_NUMBER_ID")
FACEBOOK_API_VERSION: str = os.getenv("FACEBOOK_API_VERSION")

# -----------------------------------------------------------------------------
# --- App settings ---
# -----------------------------------------------------------------------------
PHOTO_DIR: str = "photos"
