import logging

# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
from logging.handlers import TimedRotatingFileHandler  # , RotatingFileHandler

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot import echo, help_command, remove_bg, start, test
from config import BOT_TOKEN

# # Create handler that rotates at 10MB, keeps 5 backups
# handler = RotatingFileHandler(
#     "bot.log",
#     maxBytes=10 * 1024 * 1024,  # 10MB
#     backupCount=5,
# )

# One log per day, file changes at midnight with the date in the file name
handler = TimedRotatingFileHandler(
    "bot.log",
    when="midnight",
    interval=1,
    backupCount=7,  # Keep 7 days
)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)

logging.basicConfig(level=logging.INFO, handlers=[handler])
# logging.basicConfig(level=logging.INFO, handlers=[handler, logging.StreamHandler()]) # for console as well


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("test", test))
    app.add_handler(CommandHandler("echo", echo))

    app.add_handler(MessageHandler(filters.PHOTO, remove_bg))

    print("🤖 Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
