from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from config import SUDO_USERS

def sudo_filter(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS: # if message senders user id is in the sudo users list it will continue other parts
            return await func(client, message)
        else: # if message senders user id isn't in the sudo users list bot says that you are not an admin
            await client.send_message(message.chat.id , "You are not an admin :)" , reply_to_message_id=message.message_id)
    return decorator
