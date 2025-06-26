import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "7860840641").split()))

API_ID = int(os.getenv("API_ID", "23154692"))

API_HASH = os.getenv("API_HASH", "24cb1313946470840755d11ba05c51a3")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7484507364:AAEgdBVxjTbxUReaKKXBxxk3ADedFJ4bP1Y")

OWNER_ID = int(os.getenv("OWNER_ID", "7860840641"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002325511325").split()))

RMBG_API = os.getenv("RMBG_API", "VegrZSZEnnAsufcGsaxECDv6")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ditamelia711:Irawanoni02@bot-db.i4x9n1y.mongodb.net/?retryWrites=true&w=majority&appName=bot-db")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002325511325"))
