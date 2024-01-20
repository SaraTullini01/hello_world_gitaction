# get_channel_members.py

from telegram import Bot
from telegram.error import TelegramError

TELEGRAM_BOT_TOKEN = "6653294032:AAH3Bn8rEbPPNbL7IC6FfEahAXbZ4Q6EZZM"
CHANNEL_ID = -1001993783434

bot = Bot(TELEGRAM_BOT_TOKEN)

def get_channel_members_ids(channel_id):
    try:
        # Ottieni gli oggetti ChatMember
        chat_members = bot.get_chat_members(channel_id)

        # Ottieni gli ID dei membri
        member_ids = [member.user.id for member in chat_members]

        return member_ids
    except TelegramError as e:
        print(f"Errore durante il recupero degli iscritti del canale: {e}")
        return []

channel_member_ids = get_channel_members_ids(CHANNEL_ID)
print("ID dei membri del canale:", channel_member_ids)
