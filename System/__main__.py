import glob
from System.__init__ import bot
from sys import argv
from telethon import TelegramClient
from System.zypherConfig import Var
from System.utils import load_module, start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from System import CMD_HNDLR

ZASSIST = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(ZASSIST, f"**Zʏᴘʜᴇʀ X ʜᴀs ʙᴇᴇɴ ᴅᴇᴘʟᴏʏᴇᴅ, ᴅᴏ ᴠɪsɪᴛ @ZypherSupport !!.\n𝚂𝙴𝙽𝙳** `{CMD_HNDLR}alive` **𝚃𝙾 𝚂𝙴𝙴 𝙱𝙾𝚃 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙾𝚁 𝙽𝙾𝚃.**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Zypher has been deployed! ")

print("Setting up TGBot")
path = "plugins/mybot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print(
    """
                ----------------------------------------------------------------------
                    Zʏᴘʜᴇʀ X ʜᴀs ʙᴇᴇɴ ᴅᴇᴘʟᴏʏᴇᴅ, ᴅᴏ ᴠɪsɪᴛ @ZypherSupport !!
                    ᴢʏᴘʜᴇʀ ᴠᴇʀ: V1.0
                    ©ᴛᴇᴀᴍ ᴢʏᴘʜᴇʀ
                ----------------------------------------------------------------------
"""
)
bot.loop.run_until_complete(startup_log_all_done())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
#now ok
