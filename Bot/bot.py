from pyrogram import Client
from pyromod import listen
from config import API_HASH, API_ID , BOT_TOKEN

bot = Client(
    ':memory:', # it won't save any "*.session" file on the directory and will be on memory
    API_ID, # user api id
    API_HASH, # user api hash
    bot_token=BOT_TOKEN, # bot token that user wants to start the bot on it
    plugins = dict(root="handlers"), # imports plugins from 'handlers' directory 
)

bot.run() # runs the bot