# coding: utf-8
# -----------------------------------------------------------------------------
# --- Typing ---
# -----------------------------------------------------------------------------
from typing import Any, Dict, Optional

# -----------------------------------------------------------------------------
# --- Requests ---
# -----------------------------------------------------------------------------
import requests

# -----------------------------------------------------------------------------
# --- Logger ---
# -----------------------------------------------------------------------------
from loguru import logger

# -----------------------------------------------------------------------------
# --- Config ---
# -----------------------------------------------------------------------------
from config import ACCESS_TOKEN, FACEBOOK_API_VERSION, PHONE_NUMBER_ID


def send_message(to: str, message: str) -> Optional[Dict[str, Any]]:
    """Send text message via WhatsApp API"""
    url = f"https://graph.facebook.com/" \
          f"{FACEBOOK_API_VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            logger.error(f"Failed to send message to {to}: {response.text}")
        return response.json()
    except Exception as error:
        logger.error(f"Error in send_message: {error}")
        return None
