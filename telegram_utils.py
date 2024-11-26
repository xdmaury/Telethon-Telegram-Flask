from time import sleep
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
from config import API_ID, API_HASH
import os
from datetime import datetime

async def send_message(user_id, message):
    async with TelegramClient(os.environ.get('TG_SESSION', 'replier'), API_ID, API_HASH) as client:
        try:
            print(f"Sending message to {user_id}...")
            await client.send_message(user_id, message)
            print(f"Message sent to: {user_id}")
        except FloodWaitError as e:
            print(f"Flood wait error: sleeping for {e.seconds} seconds...")
            sleep(e.seconds)
        except Exception as e:
            print(f"Error sending message to {user_id}: {e}")
            raise

async def start():
    now = datetime.now()
    await send_message("me", f"{now} - API - started")
