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

shayri = [ " 🌺बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।🌺 \n\n🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀 ",
           " 🌺मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।🌺 \n\n🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀 " ]

@app.on_message(
    filters.command(shayri)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(shayri),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨𝐒υρρσɾ𝐓✨", url=f"https://t.me/TKS_JOIN"),
                     ]
            ]
        ),
    )

@app.on_message(
    filters.command(shayri)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(shayri),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💘𝐂ԋαɳɳҽ𝐋💘", url=f"https://t.me/TKS_JOIN"),
                     ]
            ]
        ),
    )