import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_NAME = getenv("BOT_NAME")
WEB_SITE = getenv("WEB_SITE")
LOG_CHANNEL = int(getenv("LOG_CHANNEL"))