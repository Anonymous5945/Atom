import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os
from tobrot import (
    DOWNLOAD_LOCATION,
    TG_BOT_TOKEN,
    APP_ID,
    API_HASH,
    AUTH_CHANNEL,
    EXEC_CMD_TRIGGER,
    Eval_CMD_TRIGGER,
    Save_CMD_TRIGGER
)

from pyrogram import Client, Filters, MessageHandler, CallbackQueryHandler

from Atom.translate import (
    trait_message_f
)

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    app = Client(
        "LeechBot",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=343
    )
    #
    incoming_message_handler = MessageHandler(
        trait_message_f,
        filters=Filters.command([Save_CMD_TRIGGER]) & Filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(trait_message_handler) 
