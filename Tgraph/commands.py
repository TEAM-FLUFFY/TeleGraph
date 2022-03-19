from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random




START_MESSAGE= """
𝙃𝙖𝙞 {},
𝙸 𝙰𝚖 𝙰 𝙿𝚛𝚎 𝙵𝚞𝚗𝚌𝚝𝚒𝚘𝚗𝚎𝚍 𝚁𝚘𝚋𝚘𝚝 𝙽𝚊𝚖𝚎𝚍,  <a href=https://t.me/EFX_TGRAPHbot>𝑇𝑔𝑟𝑎𝑝ℎ</a>!
<a href='t.me/EFX_TGRAPHbot'>𝑆𝑡𝑎𝑟𝑡 𝑀𝑒</a>,🟡𝙏𝙝𝙚𝙣 𝙎𝙚𝙚 𝙈𝙮 𝙋𝙤𝙬𝙚𝙧𝙨✨️
➖➖➖➖➖➖➖➖➖➖➖➖➖
©MᴀɪɴᴛᴀɪɴᴇD Bʏ:<a href='tg://user?id=5133623467'><b>✫𝐴𝑡ℎ𝑖𝑓 𝗧𝗚 [ᵒⁿˡⁱⁿᵉ]🇦🇹 : 𝑒𝑥𝑎𝑚📚</b></a> .</b>
"""




@Client.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    await msg.reply_photo(
        photo="https://telegra.ph/file/6c890b13e27c0f219a015.jpg"
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
