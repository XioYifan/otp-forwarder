# OTP Forwarder Bot

Bot ini menggunakan [Telethon](https://docs.telethon.dev/) untuk mem-forward pesan
dari bot tertentu (`Telkom Akses`) ke channel pribadi (`OTP Portal`).

## Cara Jalankan di Lokal
1. Install library
pip install -r requirements.txt
3. Buat file `.env` atau set environment variables:
API_ID=18384047
API_HASH=3c1b3ad3a98a584b10de2ebe97f3335a
SOURCE_BOT=HCMTelkomAksesBot
TARGET_CHANNEL=-1003177148900
4. Jalankan bot:
python forward_bot_to_channel.py

## Deploy di Render
- Tambahkan Environment Variables di Render Dashboard:
- API_ID
- API_HASH
- SOURCE_BOT
- TARGET_CHANNEL
