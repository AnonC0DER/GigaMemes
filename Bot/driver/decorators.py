from typing import Callable
from pyrogram import Client
from pyrogram.types import Message
from config import SUDO_USERS

def sudo_filter(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return decorator
