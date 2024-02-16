from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/7154ff8b7d6ab9f343f1e.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/7154ff8b7d6ab9f343f1e.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tbcbotschat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tbc_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5090817443").split()))


FAILED = "https://graph.org/file/7154ff8b7d6ab9f343f1e.jpg"
