from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
ℎ𝑒𝑦 𝑑𝑒𝑎𝑟 {} 𝑏𝑟𝑜 𝑚𝑦 𝑛𝑎𝑚𝑒 𝑖𝑠 ᴅᴇᴀᴅ ᴘᴏᴏʟ 𝑖𝑎𝑚 𝑒𝑎𝑠𝑦&𝑝𝑜𝑤𝑒𝑟 𝑓𝑢𝑙𝑙 𝑏𝑜𝑡
➖➖➖➖➖➖➖➖➖➖➖➖➖
©MᴀɪɴᴛᴀɪɴᴇD Bʏ:<a href='tg://user?id=5133623467'><b>✫𝐴𝑡ℎ𝑖𝑓 𝗧𝗚 [ᵒⁿˡⁱⁿᵉ]🇦🇹 : 𝑒𝑥𝑎𝑚📚</b></a> .</b>
"""




@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/b8966d06b16c46becf83a.jpg"
    )





    await msg.reply_text(
        text=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝑎𝑏𝑜𝑢𝑡", callback_data="about"),
            InlineKeyboardButton("ℎ𝑜𝑤 𝑡𝑜 𝑢𝑠𝑒?", url="https://t.me/T_Graph_U_s_e") 
            ]]
            )
        )


@Client.on_callback_query()
async def cb(bot, msg):
    if msg.data == "about":
        await msg.answer("""𝐶𝑟𝑒𝑎𝑡𝑒𝑟 : @KAAVAL_KAARAN_tg
𖣘 𝐵𝑜𝑡 : 𝙸𝙽𝙳𝙸𝙰𝙽""", show_alert=True)
