# WhatsApp Photo Storage Bot

A WhatsApp bot that receives photos from users and saves them.

## Project Structure

```
├── app.py                      # Main Flask webhook application
├── config.py                   # Configuration and environment variables
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create manually)
├── services/
│   ├── photo_service.py        # Photo download and storage logic
│   └── whatsapp_service.py     # WhatsApp API communication
├── handlers/
│   └── message_handler.py      # Message processing logic
├── photos/                     # Directory for saved photos (auto-created)
└── README.md                   # This file
```

## Requirements

- Python 3.11+
- WhatsApp Business API access
- Meta Developer Account
- Public webhook URL (ngrok or server)

## Installation

### 1. Clone or download the project files

```bash
git clone https://github.com/vaskinb/watsapp_photo_sender.git
cd watsapp_photo_sender
```
### 2. Create file `.env` based on `.env.example`:

```bash
cp .env.example .env
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up WhatsApp Business API

1. Create a [Meta Developer Account](https://developers.facebook.com/)
2. Create a new app and add WhatsApp Business API
3. Get your access token and phone number ID
4. Set up webhook URL in Meta Developer Console

### 5. Create environment file

Create a `.env` file in the project root:

```env
VERIFY_TOKEN=your_webhook_verify_token
ACCESS_TOKEN=your_whatsapp_access_token
PHONE_NUMBER_ID=your_phone_number_id
```

## Usage

### Start the bot:

```bash
python app.py
```

The bot will start on `http://0.0.0.0:5000`

### Webhook Endpoints:

- `GET /webhook` - Webhook verification endpoint
- `POST /webhook` - Receive WhatsApp messages

### Bot Functionality:

- **Photo Messages**: Automatically downloads and saves photos to `photos/` directory
- **Text Messages**: Responds with instructions to send photos
- **Automatic Responses**: Confirms when photos are successfully saved

## Configuration

### Environment Variables:

- `VERIFY_TOKEN` - Token for webhook verification
- `ACCESS_TOKEN` - WhatsApp Business API access token  
- `PHONE_NUMBER_ID` - Your WhatsApp Business phone number ID
- `FACEBOOK_API_VERSION` - version of facebook api

### File Storage:

- Photos are saved as `{media_id}.jpg` in the `photos/` directory
- Directory is automatically created on startup
