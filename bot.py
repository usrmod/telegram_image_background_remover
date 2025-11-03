import io

from telegram import Update
from telegram.ext import ContextTypes

from bg_rem import rem_image


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""🎨 **AI Background Remover Bot**

Welcome! I use advanced AI to remove backgrounds from your images instantly.

**How to use:**
📷 Simply send me any photo
⚡ I'll process it and return a PNG with transparent background

**Need help?** Type /help
**Test the bot:** /test

_Powered by U²-Net deep learning model_""")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """📖 **Help & Commands**

**Main Feature:**
📸 Send any photo → Get transparent background PNG

**Available Commands:**
• `/start` - Welcome message and introduction
• `/help` - Show this help message
• `/test` - Check if bot is online
• `/echo <text>` - Echo your message (utility)

**How it works:**
1️⃣ Send me a photo (as image, not document)
2️⃣ Wait 2-5 seconds while AI processes
3️⃣ Receive PNG file with transparent background

**Tips:**
✅ Works best with clear subject/background separation
✅ Supports all standard image formats
✅ No file size limit (uses Telegram's 20MB limit)

**Questions?** Contact developer via resume."""
    )


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""✅ **Bot Status: Online**

🤖 Background removal service is operational
🔋 AI model loaded and ready
📡 Connected to Telegram API

Send me a photo to test!""")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Access arguments via context.args
    if context.args:
        message = " ".join(context.args)
        await update.message.reply_text(f"You said: {message}")
    else:
        await update.message.reply_text("Usage: /echo <your_message>")


async def remove_bg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔄 **Processing your image...**\n\n"
        "⏳ Removing background with AI\n"
        "⏱️ This may take 2-5 seconds"
    )

    try:
        picture = update.message.photo[-1]
        picture_id = await context.bot.get_file(picture.file_id)

        picture_bytes = io.BytesIO()
        await picture_id.download_to_memory(picture_bytes)

        output = rem_image(picture_bytes.getvalue())

        await context.bot.send_document(
            chat_id=update.message.chat_id,
            document=output,
            filename="transparent_background.png",
            caption="✅ **Background removed successfully!**\n\n"
            "📄 Format: PNG with alpha channel\n"
            "🎨 Transparent background\n"
            "💾 Ready to use in any design tool\n\n"
            "_Send another photo to process more images_",
        )

    except Exception as e:
        await update.message.reply_text(
            f"❌ **Processing failed**\n\n"
            f"Error: `{str(e)}`\n\n"
            f"**Possible causes:**\n"
            f"• Image format not supported\n"
            f"• File too large (>20MB)\n"
            f"• Temporary server issue\n\n"
            f"Please try again or contact support."
        )


async def img_to_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("converting your single image to a pdf")

    try:
        picture = update.message.photo[-1]
        picture_id = await context.bot.get_file(picture.file_id)

        picture_bytes = io.BytesIO()
        await picture_id.download_to_memory(picture_bytes)

        pdf_output = single_image_to_pdf(picture_bytes.getvalue())

        await update.message.reply_document(
            document=pdf_output, filename="from_image.pdf", caption="Here is your pdf"
        )
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
