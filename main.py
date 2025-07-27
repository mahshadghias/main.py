import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
import telegram

TOKEN = os.environ.get("TOKEN")

app = Flask(__name__)
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

@app.route('/')
def home():
    return 'ربات زنده است! 🩵'

@app.route(f"/{TOKEN}", methods=['POST'])
def receive_update():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok', 200

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام مهشاد! ربات من روشنه 😄🩵")

dispatcher.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
