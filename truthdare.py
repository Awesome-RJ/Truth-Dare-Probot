import requests
import rapidjson as json
from PIL import Image
import os
import asyncio
import re
from config import bot_token
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


eliana = Client(
    ":memory:",
    bot_token="1708916681:AAGLHizozd7ghdacWQLTcZRkkFFV2PEMbRc",
    api_id=2114829,
    api_hash="e90ddf1f46ac58ee0c267eff1e0548de",
)



messageprivate = '''
Trust & Dare\n Using Elaina Api from @elianacommunity\n Press /help to Enjoy :)
'''

messagegroup = '''
Hi, I'm Truth And Dare
'''





@eliana.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(_, message):
    self = await eliana.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Support by", url="https://t.me/elianacommunity"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))


@eliana.on_message(filters.command("help"))
async def help_command(_, message):
    help_text = """
    **Eliana is a Truth&Dare Game which uses @elianacommunity's Elaina Api.**\n
•/truth :for random truth 
•/dare :for random dare  .
"""
    self = await eliana.get_me()
    busername = self.username

    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Click here",
                url=f"t.me/{username}?start=help")]])
        await message.reply("Contact me in PM",
                            reply_markup=buttons)
    else:
        buttons = [[InlineKeyboardButton("Managed by", url="https://t.me/Aura_Red"),
                    InlineKeyboardButton('Elaina Api', url=f"https://elianaapi.herokuapp.com/")]]
        await message.reply_text(help_text, reply_markup=InlineKeyboardMarkup(buttons))

@eliana.on_message(filters.command("truth"))
def truth(_, message):
    truth = requests.get("https://elianaapi.herokuapp.com/games/truth").json()
    truth = truth.get("truth")
    message.reply_text(truth)

@eliana.on_message(filters.command("dare"))
def dare(_, message):
    dare = requests.get("https://elianaapi.herokuapp.com/games/dares").json()
    dare = dare.get("dare")
    message.reply_text(dare)

print(
    """
Truth and dare enjoy
"""
)


eliana.run()


