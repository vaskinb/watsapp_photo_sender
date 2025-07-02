# coding: utf-8
import os
# -----------------------------------------------------------------------------
# --- Typing ---
# -----------------------------------------------------------------------------
from typing import Optional

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
from config import ACCESS_TOKEN, PHOTO_DIR

# -----------------------------------------------------------------------------
# --- Create photo directory ---
# -----------------------------------------------------------------------------
os.makedirs(PHOTO_DIR, exist_ok=True)


def download_photo(media_id: str) -> Optional[str]:
    """Downloads photos from WhatsApp"""
    try:
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

        # ---------------------------------------------------------------------
        # --- Get  URL of a media file ---
        # ---------------------------------------------------------------------
        metadata_url = f"https://graph.facebook.com/v18.0/{media_id}"
        response = requests.get(metadata_url, headers=headers)

        if response.status_code != 200:
            logger.error(f"Failed to get media URL for media_id={media_id}")
            return None

        media_url = response.json().get("url")
        if not media_url:
            logger.error(f"No media URL found for media_id={media_id}")
            return None

        # ---------------------------------------------------------------------
        # --- Download file ---
        # ---------------------------------------------------------------------
        file_response = requests.get(media_url, headers=headers)
        if file_response.status_code != 200:
            logger.error(
                f"Failed to download media file: {file_response.status_code}")
            return None

        # ---------------------------------------------------------------------
        # --- Save to directory ---
        # ---------------------------------------------------------------------
        filename = os.path.join(PHOTO_DIR, f"{media_id}.jpg")
        with open(filename, "wb") as f:
            f.write(file_response.content)

        logger.info(f"Photo saved: {filename}")
        return filename

    except Exception as error:
        logger.error(f"Error in download_photo: {error}")
        return None
