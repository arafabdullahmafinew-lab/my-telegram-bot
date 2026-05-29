from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=10000)

async def start(update, context):
    text = "আসসালামু আলাইকুম! নিচের বাটনে ক্লিক করে অ্যাপ ওপেন করুন 😎😍"
    keyboard = [[InlineKeyboardButton("OPEN APP", web_app=WebAppInfo(url="https://yourearningbdbot.blogspot.com"))]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

if __name__ == '__main__':
    threading.Thread(target=run).start()
    bot = ApplicationBuilder().token("8449272155:AAEig_CVY3IBlcgkEK-IlDJaS8kKgmUS9GA").build()
    bot.add_handler(CommandHandler("start", start))
    bot.run_polling()
