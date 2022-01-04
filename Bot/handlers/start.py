from pyrogram import Client, filters
from driver.decorators import sudo_filter
from config import BOT_USERNAME, BOT_NAME, WEB_SITE

@Client.on_message(filters.command(['start' , f'start{BOT_USERNAME}']) & filters.group)
@sudo_filter
async def start_group(client , message):
    await message.reply("Alive as fuck")

@Client.on_message(filters.command(['start' , f'start{BOT_USERNAME}']) & filters.private)
@sudo_filter
async def start_private(client , message):
    await message.reply(f"Hey master,\nWelcome to {BOT_NAME} you can use /sendmeme to send a new meme to your [Website]({WEB_SITE})")