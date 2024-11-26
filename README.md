# Telethon-Telegram-Flask

This is a RESTful API built with Flask, designed to integrate with Telegram using the Telethon library. The API initializes a Telegram session and provides a POST route that allows sending messages to specific users, offering a simple and efficient way to automate interactions with the Telegram platform.

# Usage Example

Here’s an example of how to use the API to send a message to a specific Telegram user:

Endpoint:
```bash
    POST http://localhost:5001/send-message
```

Request Body (JSON):
```json
{
  "user_id": "0123456",
  "message": "Hello from Flask and Telethon!"
}
```

Technologies Used:
- Python 3.8+
- Flask for building the API.
- Telethon for interacting with the Telegram API.
- dotenv for managing environment variables.

Observations:

- Avoid Using Personal Accounts: It is strongly advised to refrain from using personal Telegram accounts for this purpose, as it may lead to account bans due to excessive or automated activity.
- Extend Message Intervals: To reduce the risk of triggering spam detection, ensure that there is a sufficiently long interval between sending messages. The longer the delay, the lower the chance of being flagged.