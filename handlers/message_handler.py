# coding: utf-8
# -----------------------------------------------------------------------------
# --- Typing ---
# -----------------------------------------------------------------------------
from typing import Any, Dict

# -----------------------------------------------------------------------------
# --- Logger ---
# -----------------------------------------------------------------------------
from loguru import logger

# -----------------------------------------------------------------------------
# --- Services ---
# -----------------------------------------------------------------------------
from services.photo_service import download_photo
from services.whatsapp_service import send_message


def handle_image_message(message: Dict[str, Any], from_number: str) -> None:
    """Processes image messages"""

    # -------------------------------------------------------------------------
    # --- Get media id ---
    # -------------------------------------------------------------------------
    media_id = message.get("image", {}).get("id")
    if not media_id:
        logger.warning("Image message missing media_id")
        send_message(from_number, "Сталася помилка. Спробуйте ще.")
        return

    # -------------------------------------------------------------------------
    # --- Download photo ---
    # -------------------------------------------------------------------------
    file_path = download_photo(media_id)

    # -------------------------------------------------------------------------
    # --- Send message ---
    # -------------------------------------------------------------------------
    if file_path:
        send_message(from_number, "Фото збережено, дякуємо!")
    else:
        send_message(from_number, "Сталася помилка. Спробуйте ще.")


def handle_text_message(message: Dict[str, Any], from_number: str) -> None:
    """Processes text message"""
    send_message(from_number, "Вітаємо! Надішліть фото, щоб зберегти його.")


def handle_message(message: Dict[str, Any]) -> None:
    """Main message processing function"""

    # -------------------------------------------------------------------------
    # --- Get message info ---
    # -------------------------------------------------------------------------
    from_number = message.get("from")
    msg_type = message.get("type")

    if not from_number or not msg_type:
        logger.warning("Missing from_number or type")
        return

    logger.info(f"New {msg_type} message from {from_number}")

    # -------------------------------------------------------------------------
    # --- Handle message ---
    # -------------------------------------------------------------------------
    if msg_type == "image":
        handle_image_message(message, from_number)
    elif msg_type == "text":
        handle_text_message(message, from_number)
    else:
        logger.info(f"Ignoring message type: {msg_type}")


def process_webhook_data(data: Dict[str, Any]) -> None:
    """Processes data from webhook"""
    entries = data.get("entry", [])

    for entry in entries:
        changes = entry.get("changes", [])

        for change in changes:
            # -----------------------------------------------------------------
            # --- Get message list ---
            # -----------------------------------------------------------------
            value = change.get("value", {})
            messages = value.get("messages", [])

            for message in messages:
                # -------------------------------------------------------------
                # --- Handle message ---
                # -------------------------------------------------------------
                handle_message(message)
