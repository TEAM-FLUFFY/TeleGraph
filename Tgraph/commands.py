from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random




START_MESSAGE="""hey {} എന്റെ പേര് <a href=https://t.me/FluffyPyroGramBot>𝙵𝙻𝚄𝙵𝙵𝚈 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>, 🔰മച്ചാനെ എന്റെ പണി കഴിഞ്ഞിട്ടില്ല അതുകൊണ്ട് RePo✅️ പ്രൈവറ്റ് ആണ് Work കഴിഞ്ഞിട്ട് public ആക്കും
"""
       


ALL_PIC = [
 "https://telegra.ph/file/7313f50315f1914e5b43f.jpg",
 "https://telegra.ph/file/cac42a836652d9314a807.jpg",
]

@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=START_MESSAGE.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton ("𝙳𝙴𝚅", url="https://t.me/KAAVAL_KAARAN_tg"),
           ],[
           InlineKeyboardButton ("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴?", return await query.answer("𝙸𝚃'𝚂 𝚂𝙸𝙼𝙿𝙻𝙴 𝚂𝙴𝙽𝚃 𝙼𝙴 5𝙼𝙱 𝙿𝙸𝙲𝚃𝚄𝚁𝙴 𝙸 𝙴𝙳𝙸𝚃 𝙰𝙽𝙳 𝚂𝙴𝙽𝚃 𝚈𝙾𝚄𝚁 𝙵𝙸𝙻𝙴.", show_alert=True)
          ]]
          )
    )
