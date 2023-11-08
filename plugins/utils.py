#Animexyz

import os
import asyncio
from pyrogram.types import Message
from bot import Bot
from helper_func import get_messages
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_message(filters.command('user') & filters.private & filters.user(1803603990))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")
