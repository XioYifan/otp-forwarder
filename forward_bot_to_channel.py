# forward_bot_to_channel.py
from telethon import TelegramClient, events
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

# isi ini:
api_id = 18384047           # dari my.telegram.org
api_hash = '3c1b3ad3a98a584b10de2ebe97f3335a' # dari my.telegram.org
session_name = 'otp_forwarder'  # nama file session
TARGET_CHANNEL = -1003177148900   # bisa juga invite link atau id (contoh: -1001234567890)
SOURCE_BOT = 'HCMTelkomAksesBot' # username tanpa @ atau bisa pakai id

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(from_users=SOURCE_BOT))
async def handler(event):
    try:
        # forward message ke channel
        await client.forward_messages(TARGET_CHANNEL, event.message)
        logging.info(f'Forwarded message id {event.message.id}')
    except Exception as e:
        logging.exception('Gagal forward pesan: %s', e)

async def main():
    await client.start()  # akan meminta nomor + kode OTP saat pertama kali
    print('Userbot berjalan. Mendengarkan pesan dari', SOURCE_BOT)
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
