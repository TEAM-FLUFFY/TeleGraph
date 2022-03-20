from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
𝙷𝙴𝚈 𝙳𝙴𝙰𝚁 {} 𝙱𝚁𝙾 𝙸𝙰𝙼 𝙳𝙴𝙰𝙳 𝙿𝙾𝙾𝙻 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁 𝙸𝚂 𝚃𝙶𝚁𝙰𝙿𝙷
"""




@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/b8966d06b16c46becf83a.jpg"
    )





    await msg.reply_text(
        text=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝙰𝙱𝙾𝚄𝚃", callback_data="about"),
            InlineKeyboardButton("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴", url="https://t.me/T_Graph_U_s_e") 
            ]]
            )
        )



@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "about":
        await msg.answer("""𖣘𝙲𝚁𝙴𝙰𝚃𝙴𝚁 : ᴇxᴀᴍ എഴുതാൻ പോകുന്നു
𑁍 𝙺𝙰𝙽𝙶𝙴𝙳 𝙱𝚈 : 𝙏𝙂 𝙋𝙐𝙎𝙃𝙋𝘼 𝙍𝙀𝙅𝙐🇮🇳[OFFLINE] #CrimeMalayalamMoviez
𖣔𝙱𝙾𝚃 : 𝙸𝙽𝙳𝙸𝙰𝙽""", show_alert=True)

