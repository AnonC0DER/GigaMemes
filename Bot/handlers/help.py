from pyrogram import Client, filters, types
from pyrogram.types.messages_and_media.message import Message
from driver.functions import *
from config import BOT_USERNAME
######################################


@Client.on_message(filters.command('help'))
async def help(client, message: Message):
    '''Command lists'''

    await client.send_message(message.chat.id, f'''
Commands list :
- register -> /register
- Create new meme -> /create_meme
- Create new tag -> /create_tag
- Post a vote -> /vote
- Post a comment -> /comment

Enjoy :)
@{BOT_USERNAME}''', reply_markup=types.InlineKeyboardMarkup(
        [

            [
                types.InlineKeyboardButton('GitHub', url='https://github.com/AnonC0DER/GigaMemes')
            ]

        ]
    ),  )