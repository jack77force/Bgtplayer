from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time

from Bikash import app
from Bikash.utils.bgtmusic.bk import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

shayri = [ "Hello Guys",
"Now You See Me" ]

@app.on_message(
    filters.command("shayri")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def bikash(client: Client, message: Message):
    await message.reply_text(text = random.choice(shayri),
        reply_markup=InlineKeyboardMarkup(
            [
                
                [
                    InlineKeyboardButton(
                        "🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 🥀", url=f"https://t.me/mission_successs"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 🥀", url=f"https://t.me/Current_Affairs_Zone_2")
                ]
            ]
        ),
    )
