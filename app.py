# coding: utf-8
# -----------------------------------------------------------------------------
# --- Typing ---
# -----------------------------------------------------------------------------
from typing import Any

# -----------------------------------------------------------------------------
# --- Flask ---
# -----------------------------------------------------------------------------
from flask import Flask, jsonify, request

# -----------------------------------------------------------------------------
# --- Logger ---
# -----------------------------------------------------------------------------
from loguru import logger

# -----------------------------------------------------------------------------
# --- Config ---
# -----------------------------------------------------------------------------
from config import VERIFY_TOKEN

# -----------------------------------------------------------------------------
# --- Handlers ---
# -----------------------------------------------------------------------------
from handlers.message_handler import process_webhook_data

app = Flask(__name__)


@app.route("/webhook", methods=["GET"])
def verify_webhook() -> tuple[str, int]:
    """Webhook verification for WhatsApp"""
    if (
        request.args.get("hub.mode") == "subscribe"
        and request.args.get("hub.verify_token") == VERIFY_TOKEN
    ):
        logger.info("Webhook verified successfully")
        return request.args.get("hub.challenge"), 200

    logger.warning("Webhook verification failed")
    return "Unauthorized", 403


@app.route("/webhook", methods=["POST"])
def handle_webhook() -> tuple[Any, int]:
    """Processing messages from WhatsApp"""
    try:
        data = request.get_json()
        if not data:
            logger.error("No JSON data in webhook POST")
            return jsonify({"error": "No data"}), 400

        process_webhook_data(data)
        return jsonify({"status": "ok"}), 200

    except Exception as error:
        logger.exception("Exception in webhook handler")
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    logger.info("Starting WhatsApp webhook server...")
    app.run(debug=False, host="0.0.0.0", port=5000)
