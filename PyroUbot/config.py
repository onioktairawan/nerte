import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "1324779186").split()))

API_ID = int(os.getenv("API_ID", "23581804"))

API_HASH = os.getenv("API_HASH", "49fd7d9ac9aecb487c343a0c1156f8d2")

BOT_TOKEN = os.getenv("BOT_TOKEN", "77568865887:AAFZpGqtCCmTaXGxwo7lGBtFs0z8bBCD5Yo")

OWNER_ID = int(os.getenv("OWNER_ID", "1324779186"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002325511325").split()))

RMBG_API = os.getenv("RMBG_API", "VegrZSZEnnAsufcGsaxECDv6")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ditamelia711:Irawanoni02@bot-db.i4x9n1y.mongodb.net/?retryWrites=true&w=majority&appName=bot-db")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002325511325"))
