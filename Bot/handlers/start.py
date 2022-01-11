from pyrogram import Client, filters, types
from config import BOT_USERNAME

# Works only on private chat
@Client.on_message(filters.command(['start' , f'start{BOT_USERNAME}']) & filters.private) 
async def start_private(client , message):
    # sends start message for private
    await message.reply(f'''
Hello {message.from_user.first_name}. \n
Here you can create and post your memes to the website.
Please send /help to get commands list. 

@{BOT_USERNAME}''', reply_markup=types.InlineKeyboardMarkup(
        [

            [
                types.InlineKeyboardButton('GitHub', url='https://github.com/AnonC0DER/GigaMemes')
            ]

        ]
    ),  ) 