# get_channel_members.py

from telegram import Bot
from telegram.error import TelegramError

TELEGRAM_BOT_TOKEN = "IlTuoTokenDelBot"
CHANNEL_ID = -1001234567890

bot = Bot(TELEGRAM_BOT_TOKEN)

def get_channel_members_ids(channel_id):
    try:
        members = bot.get_chat_members(channel_id)
        member_ids = [member.user.id for member in members]
        return member_ids
    except TelegramError as e:
        print(f"Errore durante il recupero degli iscritti del canale: {e}")
        return []

channel_member_ids = get_channel_members_ids(CHANNEL_ID)
print("ID dei membri del canale:", channel_member_ids)
