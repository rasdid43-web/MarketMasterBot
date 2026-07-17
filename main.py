import os
import asyncio

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في MarketMasterBot\n\n"
        "الأوامر:\n"
        "/gold - تحليل الذهب\n"
        "/crypto - تحليل العملات الرقمية\n"
        "/forex - تحليل الفوركس"
    )


async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 تحليل الذهب قريباً...")


async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🪙 تحليل العملات الرقمية قريباً...")


async def forex(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💱 تحليل الفوركس قريباً...")


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gold", gold))
    app.add_handler(CommandHandler("crypto", crypto))
    app.add_handler(CommandHandler("forex", forex))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
