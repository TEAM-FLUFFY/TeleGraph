from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
๐ท๐ด๐ ๐ณ๐ด๐ฐ๐ {} ๐ฑ๐๐พ ๐ธ๐ฐ๐ผ ๐ณ๐ด๐ฐ๐ณ ๐ฟ๐พ๐พ๐ป ๐ผ๐ ๐ฟ๐พ๐๐ด๐ ๐ธ๐ ๐๐ถ๐๐ฐ๐ฟ๐ท
"""




@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/b8966d06b16c46becf83a.jpg"
    )





    await msg.reply_text(
        text=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("๐ฐ๐ฑ๐พ๐๐", callback_data="about"),
            InlineKeyboardButton("๐ท๐พ๐ ๐๐พ ๐๐๐ด", url="https://t.me/T_Graph_U_s_e") 
            ]]
            )
        )



@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "about":
        await msg.answer("""๐ฃ๐ฒ๐๐ด๐ฐ๐๐ด๐ : แดxแดแด เดเดดเตเดคเดพเตป เดชเตเดเตเดจเตเดจเต
๐ ๐บ๐ฐ๐ฝ๐ถ๐ด๐ณ ๐๐ด๐ฟ๐พ : ๐๐ ๐๐๐๐๐๐ผ ๐๐๐๐๐ฎ๐ณ[OFFLINE]
๐ฃ๐ฑ๐พ๐ : ๐ธ๐ฝ๐ณ๐ธ๐ฐ๐ฝ""", show_alert=True)

