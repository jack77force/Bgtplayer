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


@app.on_message(
    filters.command("shayri")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def bikash(client: Client, message: Message):
    await message.reply_text(text = random.choice(shayri),
        photo=f"https://telegra.ph/file/47965cd5bedfb980059a6.jpg",
        caption=f"""🥀 𝐃𝐞𝐯𝐢𝐥 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝐃𝐞𝐯𝐢𝐥 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐋𝐢𝐯𝐞 𝐐𝐮𝐢𝐳 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 & 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 [𝐃𝐞𝐯𝐢𝐥](https://t.me/Monu_Gupta_01)""",
        caption=f"""Hello Guys"""
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
