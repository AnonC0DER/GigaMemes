from pyrogram import Client, filters, types
from driver.decorators import sudo_filter
from config import BOT_USERNAME, BOT_NAME, WEB_SITE

# Works only on private chat
@Client.on_message(filters.command(['start' , f'start{BOT_USERNAME}']) & filters.private) 
@sudo_filter # filters sudo users
async def start_private(client , message):
    # sends start message for private
    await message.reply(f'''
Hello {message.from_user.first_name} Admin. \n
Here you can create and post your memes to the website.
Please send /create to create a new meme. 

@{BOT_USERNAME}''', reply_markup=types.InlineKeyboardMarkup(
        [

            [
                types.InlineKeyboardButton('GitHub', url='https://github.com/AnonC0DER/GigaMemes')
            ]

        ]
    ),  ) 