import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("درحال ارسال پیام ناشناس به «مهشاد» هستی. میتونی هر حرف یا انتقادی که تو دلت هست رو بگی چون پیامت بصورت کاملا ناشناس ارسال میشه!")

def main():
    TOKEN = os.environ.get("توکن ربات موجود نیست")
    if not TOKEN:
        print("TOKEN")
        return

    keep_alive()

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
