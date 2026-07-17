from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "@Rr147258-"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في MarketMasterBot\n\n"
        "الأوامر:\n"
        "/gold - تحليل الذهب\n"
        "/crypto - تحليل العملات الرقمية\n"
        "/forex - تحليل الفوركس"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
