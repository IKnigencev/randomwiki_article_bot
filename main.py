import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

from utils import get_title_and_link


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def get_random_article(update, context):
    '''Функция отправки сообщения пользваотелю.'''
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_title_and_link())


def wake_up(update, context):
    '''Функция при активации бота.'''
    chat = update.effective_chat
    name = update.message.chat.first_name
    text = f'Привет, {name}. Посмотри, какую статью на википедии я тебе нашел!'
    button = ReplyKeyboardMarkup(
        [['/newarticle']],
        resize_keyboard=True
    )

    context.bot.send_message(
        chat_id=chat.id,
        text=text,
        reply_markup=button
    )

    context.bot.send_photo(chat.id, get_random_article())


def main():

    updater = Updater(token=TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(
        CommandHandler('newarticle', get_random_article))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
