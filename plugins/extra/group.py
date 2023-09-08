from pyrogram import Client, filters

from Bikash import app
from Bikash.utils.bgtmusic.bk import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("group")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def bikash(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1e5e9c8021f5932cc3b57.jpg",
        caption=f"""🥀 𝐃𝐞𝐯𝐢𝐥 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝐃𝐞𝐯𝐢𝐥 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐋𝐢𝐯𝐞 𝐐𝐮𝐢𝐳 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 & 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 [𝐃𝐞𝐯𝐢𝐥](https://t.me/Monu_Gupta_01)""",
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
