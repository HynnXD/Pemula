import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "7991421690").split()))

API_ID = int(os.getenv("API_ID", "29195279"))

API_HASH = os.getenv("API_HASH", "f7fc8826747b34739c7e588f4b3e899e")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8018326706:AAFN7MtLA7pJk75EoryvKSv_DR1FcaIqbhg")

OWNER_ID = int(os.getenv("OWNER_ID", "7991421690"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aortulsk:KxCX5EQdssavL4dm@cluster0.qsywpr2.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4917438098"))
