import datetime
from logging import getLogger
from subprocess import Popen
from subprocess import PIPE

from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request

from apis.bittrex import BittrexClient
from apis.bittrex import BittrexError
from echo.config import load_config
from echo.buttons import BUTTON1_HELP
from echo.buttons import BUTTON2_TIME
from echo.buttons import get_base_reply_keyboard
from echo.utils import debug_requests


config = load_config()

logger = getLogger(__name__)



CALLBACK_BUTTON1_LEFT = "callback_button1_left"
CALLBACK_BUTTON2_RIGHT = "callback_button2_right"
CALLBACK_BUTTON3_MORE = "callback_button3_more"
CALLBACK_BUTTON4_BACK = "callback_button4_back"
CALLBACK_BUTTON5_TIME = "callback_button5_time"
CALLBACK_BUTTON6_PRICE = "callback_button6_price"
CALLBACK_BUTTON7_PRICE = "callback_button7_price"
CALLBACK_BUTTON8_PRICE = "callback_button8_price"
CALLBACK_BUTTON_HIDE_KEYBOARD = "callback_button9_hide"


TITLES = {
    CALLBACK_BUTTON1_LEFT: "NEw ",
    CALLBACK_BUTTON2_RIGHT: "wdit ",
    CALLBACK_BUTTON3_MORE: "other ",
    CALLBACK_BUTTON4_BACK: "back ",
    CALLBACK_BUTTON5_TIME: "time ",
    CALLBACK_BUTTON6_PRICE: "BTC ",
    CALLBACK_BUTTON7_PRICE: "LTC ",
    CALLBACK_BUTTON8_PRICE: "ETH ",
    CALLBACK_BUTTON_HIDE_KEYBOARD: "sdsd ",
}


client = BittrexClient()


def get_base_inline_keyboard():
  
    keyboard = [

        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_RIGHT], callback_data=CALLBACK_BUTTON2_RIGHT),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HIDE_KEYBOARD], callback_data=CALLBACK_BUTTON_HIDE_KEYBOARD),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_MORE], callback_data=CALLBACK_BUTTON3_MORE),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard2():

    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_TIME], callback_data=CALLBACK_BUTTON5_TIME),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_PRICE], callback_data=CALLBACK_BUTTON6_PRICE),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_PRICE], callback_data=CALLBACK_BUTTON7_PRICE),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_PRICE], callback_data=CALLBACK_BUTTON8_PRICE),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_BACK], callback_data=CALLBACK_BUTTON4_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


@debug_requests
def keyboard_callback_handler(update, context):

    query = update.callback_query
    data = query.data
    now = datetime.datetime.now()

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == CALLBACK_BUTTON1_LEFT:

        query.edit_message_text(
            text=current_text,
            parse_mode=ParseMode.MARKDOWN,
        )
  
        context.bot.send_message(
            chat_id=chat_id,
            text="new mess\n\ncallback_query.data={}".format(data),
            reply_markup=get_base_inline_keyboard(),
        )
    elif data == CALLBACK_BUTTON2_RIGHT:

        query.edit_message_text(
            text="edited  {}".format(now),
            reply_markup=get_base_inline_keyboard(),
        )
    elif data == CALLBACK_BUTTON3_MORE:

        query.edit_message_text(
            text=current_text,
            reply_markup=get_keyboard2(),
        )
    elif data == CALLBACK_BUTTON4_BACK:

        query.edit_message_text(
            text=current_text,
            reply_markup=get_base_inline_keyboard(),
        )
    elif data == CALLBACK_BUTTON5_TIME:

        text = "*exact time  *\n\n{}".format(now)
        query.edit_message_text(
            text=text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard2(),
        )
    elif data in (CALLBACK_BUTTON6_PRICE, CALLBACK_BUTTON7_PRICE, CALLBACK_BUTTON8_PRICE):
        pair = {
            CALLBACK_BUTTON6_PRICE: "USD-BTC",
            CALLBACK_BUTTON7_PRICE: "USD-LTC",
            CALLBACK_BUTTON8_PRICE: "USD-ETH",
        }[data]

        try:
            current_price = client.get_last_price(pair=pair)
            text = "* kurs:*\n\n*{}* = {}$".format(pair, current_price)
        except BittrexError:
            text = "error  :(\n\happebed "
        query.edit_message_text(
            text=text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard2(),
        )
    elif data == CALLBACK_BUTTON_HIDE_KEYBOARD:

        context.bot.send_message(
            chat_id=chat_id,
            text="\n\press /start ",
            reply_markup=ReplyKeyboardRemove(),
        )


@debug_requests
def do_start(update, context):
    update.message.reply_text(
        text="Hi! ",
        reply_markup=get_base_reply_keyboard(),
    )


@debug_requests
def do_help(update, context):
    update.message.reply_text(
        text="testbott\n\n"
             "comands \n\n"
             "fgfg",
        reply_markup=get_base_inline_keyboard(),
    )


@debug_requests
def do_time(update, context):

    process = Popen(["date"], stdout=PIPE)
    text, error = process.communicate()

    if error:
        text = "erere "
    else:

        text = text.decode("utf-8")
    update.message.reply_text(
        text=text,
        reply_markup=get_base_inline_keyboard(),
    )


@debug_requests
def do_echo(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    if text == BUTTON1_HELP:
        return do_help(update=update, context=context)
    elif text == BUTTON2_TIME:
        return do_time(update=update, context=context)
    else:
        reply_text = "ID = {}\n\n{}".format(chat_id, text)
        update.message.reply_text(
            text=reply_text,
            reply_markup=get_base_inline_keyboard(),
        )


def main():
    logger.info("starting bot...")

    req = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        token='850558425:AAFLZUjeFPPG_7-9oGRtGm12qaw-1G7BxyE',
        request=req,
        #base_url=config.TG_API_URL,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

 
    info = bot.get_me()
    #logger.info(f'Bot info: {info}')


    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)

    updater.start_polling()
    updater.idle()

    logger.info("end...")


if __name__ == '__main__':
    main()
