from pyrogram import Client
from pyromod import listen
from config import API_HASH, API_ID , BOT_TOKEN

app = Client(
    ':memory:',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins = dict(root="handlers"),
)

app.run()