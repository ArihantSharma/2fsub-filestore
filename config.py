#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7533155506:AAHNMziIm1-074JpPYceXSu07tPc21o3bxE")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26634100"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9ea49405d5a93e784114c469f5ce4bbd")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002243250360"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "VØAT")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6321064549"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://lucas242158:HCXwNAkwk3DLtAkP@cluster0.taoae8u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002195629647"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002257627668"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "ʏᴏᴏ {mention} ✌🏻\nꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋꜱ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5070485868 6907806722 5560962562 711563496 6907806722").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʏᴏᴜ ᴇxᴘᴇᴄᴛ ᴛᴏ ᴜꜱᴇ ᴍᴇ, ᴡɪᴛʜᴏᴜᴛ ᴇᴠᴇɴ ᴊᴏɪɴɪɴɢ ᴍʏ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟꜱ? 😔\nᴊᴏɪɴ ᴛʜᴇ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ, ʟɪɴᴋᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{filename}</b>\n<b>• ʙʏ @YugenNetwork</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
