from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
ℎ𝑒𝑦 𝑑𝑒𝑎𝑟 {} 𝑏𝑟𝑜 𝑖𝑎𝑚 𝑇𝑔𝑟𝑎𝑝ℎ 𝑣𝑒𝑟𝑦 𝑢𝑠𝑒 𝑓𝑢𝑙 𝑏𝑜𝑡
"""



    await msg.reply_text(
        text=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝙰𝙱𝙾𝚄𝚃", callback_data="about"),
            InlineKeyboardButton("𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴?", callback_data="use") 
            ]]
            )
        )



@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "use":
        await msg.answer("""It’s simple to use me. Just send any photo or video below 5 MB and you will get the telegraph link
""", show_alert=True)



@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "about":
        await msg.answer("""CREATER ✫𝐴𝑡ℎ𝑖𝑓 𝗧𝗚 [ᵒⁿˡⁱⁿᵉ]🇦🇹
USER NAME @KAAVAL_KAARAN_tg
""", show_alert=True)
