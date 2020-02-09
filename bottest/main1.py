from telegram.ext import Updater, InlineQueryHandler, CommandHandler,Filters,MessageHandler,CallbackQueryHandler
from subprocess import Popen,PIPE


from telegram import InlineKeyboardButton,ParseMode, InlineKeyboardMarkup,ReplyKeyboardRemove,ReplyKeyboardMarkup
import requests
import re
import datetime
from buttons import BUTTON1_HELP
from buttons import BUTTON2_TIME
from buttons import get_base_reply_keyboard

import importlib
import os
import sys






'''config = load_config()

logger = getLogger(__name__)




def debug_requests(f):
	def inner(*args,**kwagrs):
		try:
			logger.info(f"callinf func{f.__name__}")
			return f(*args,**kwagrs)
		except Exception:
			logger.info(f"There is error {f.__name__}")
			raise
	return inner
'''



CALLBACK_BUTTON1_LEFT = "callback_button1_left"
CALLBACK_BUTTON2_RIGHT = "callback_button2_right"
CALLBACK_BUTTON3_MORE = "callback_button3_more"
CALLBACK_BUTTON4_BACK = "callback_button4_back"
CALLBACK_BUTTON5_TIME = "callback_button5_time"
CALLBACK_BUTTON6_PRICE = "callback_button6_price"
CALLBACK_BUTTON7_PRICE = "callback_button7_price"
CALLBACK_BUTTON8_PRICE = "callback_button8_price"
CALLBACK_BUTTON_HIDE_KEYBOARD = "callback_button9_hide"
CALLBACK_BACK_BTN  = "call_back_btn"



TITLES = {
    CALLBACK_BUTTON1_LEFT: "NEWBTN ",
    CALLBACK_BUTTON2_RIGHT: "EITBTN ",
    CALLBACK_BUTTON3_MORE: "other ",
    CALLBACK_BUTTON4_BACK: "back ",
    CALLBACK_BUTTON5_TIME: "time ",
    CALLBACK_BUTTON6_PRICE: "BTC ",
    CALLBACK_BUTTON7_PRICE: "LTC ",
    CALLBACK_BUTTON8_PRICE: "ETH ",
    CALLBACK_BUTTON_HIDE_KEYBOARD: "Hide Buttons ",
    CALLBACK_BACK_BTN :"Back"

}




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


def get_back():

	keyboard = [

        [
            InlineKeyboardButton(TITLES[CALLBACK_BACK_BTN], callback_data=CALLBACK_BACK_BTN),
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


def keyboard_callback(bot, update,chat_data=None,**kwargs):

	query = update.callback_query
	data = query.data
	now = datetime.datetime.now()

	chat_id = update.effective_message.chat_id
	current_text = update.effective_message.text
	print ( data+'--'+CALLBACK_BACK_BTN)

	if data == 'call_back_btn':
		print(current_text)
		do_new(bot=bot,update=update)
	print ('rrr')



def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
	allowed_extension = ['jpg','jpeg','png']
	file_extension = ''
	while file_extension not in allowed_extension:
		url = get_url()
		file_extension = re.search("([^.]*)$",url).group(1).lower()
	return url





def keyboard_callback_handler(bot, update,chat_data=None,**kwargs):

	query = update.callback_query
	data = query.data
	user=query.from_user
	now = datetime.datetime.now()

	chat_id = update.effective_message.chat_id
	current_text = update.effective_message.text

	if data == CALLBACK_BUTTON1_LEFT:

		query.edit_message_text(
            text=current_text,
            parse_mode=ParseMode.MARKDOWN,
        )
  
		bot.send_message(
            chat_id=chat_id,
            text="new mess\n\ncallback_query.data={}".format(data),
            reply_markup=get_base_inline_keyboard(),
        )
	elif data == CALLBACK_BUTTON2_RIGHT:
		print(chat_id)
		#bot.send_message(chat_id=chat_id,text="pjkjk ",)
		#bot.send_photo(chat_id=chat_id, photo=url)
		return start(bot=bot,update=query)
		print('5555')

		'''query.edit_message_text(
            text="edited  {}".format(now),
            reply_markup=get_base_inline_keyboard(),
        )'''

	elif data == CALLBACK_BACK_BTN:
		print(CALLBACK_BACK_BTN)
		bot.send_message(chat_id=chat_id,text="back ",)
		#bot.send_photo(chat_id=chat_id, photo=url)
		return start(bot=bot,update=query)
		#print('5555')

		'''query.edit_message_text(
            text="edited  {}".format(now),
            reply_markup=get_base_inline_keyboard(),
        )'''

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

		bot.send_message(
            chat_id=chat_id,
            text="press  /start to return buttons ",
            reply_markup=ReplyKeyboardRemove(),
        )









def start(bot, update):
	custom_keyboard = [['🔴Red Team🔴', '🔵Blue Team🔵'], 
                   ['ddd']]
	buttons = ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)

	url = get_image_url()
	chat_id = update.message.chat_id

	bot.send_photo(chat_id=chat_id, photo=url,)
	bot.send_message(
	chat_id=update.message.chat_id,
	text='New Doggo',
	reply_markup=buttons,)


def do_new(bot, update):
    url = get_image_url()
    text=update.message.text=update.message.text
   # if text=='new':
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    '''else:
    	bot.send_message(
		chat_id=update.message.chat_id,
		text='yuyuy not want ',
		)'''



def do_blueteam(bot, update):

	print ('33333')
	bot.send_message(
	chat_id=update.message.chat_id,
	text='Send Any Amount of Bip to \n 🔵Blue Team🔵',
	reply_markup=get_back(),
	)
	print ('fdf')


def do_redteam(bot, update):

	print ('2323')
	bot.send_message(
	chat_id=update.message.chat_id,
	text='Send Any Amount of Bip to \n 🔴Red Team🔴',
	reply_markup=get_back(),
	)
	print ('wewe')


def do_bnt(bot, update):
	custom_keyboard = [['top-left', 'top-right'], 
                   ['bottom-left', 'bottom-right']]
	reply_markup = ReplyKeyboardMarkup(custom_keyboard)
	bot.send_message(
	chat_id=update.message.chat_id,
	text='YTs help \n  speciyfy',
	reply_markup=reply_markup,
	)



def do_time(bot, update):
	process = Popen(["date"],stdout=PIPE)
	text,error =process.communicate()
	if error:
		text="There is error"
	else:
		text=text.decode("utf-8")
		print (text)

	bot.send_message(
	chat_id=update.message.chat_id,
	text=text,
	)
        


def do_echo(bot,update):
	chat_id = update.message.chat_id
	text = update.message.text
	if text == '🔴Red Team🔴':
		print ('red')
		return do_redteam(bot=bot,update=update)
	elif text == '🔵Blue Team🔵':
		return do_blueteam(bot=bot,update=update)
	else:
		reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
	bot.send_message(
		chat_id=chat_id,
		text=reply_text,
		reply_markup=get_base_inline_keyboard()
		)

def main():
	print('started')	
	#logger.info("Starting...")

	updater = Updater('850558425:AAFLZUjeFPPG_7-9oGRtGm12qaw-1G7BxyE')

	# info = bot.get_me()
	# logger.info(f'Bot info: {info}')


	dp = updater.dispatcher

	dp.add_handler(CommandHandler('start',start))
	dp.add_handler(CommandHandler('help',do_redteam))
	dp.add_handler(CommandHandler('time',do_bnt))



	 
    
	#dp.add_handler(MessageHandler(Filters.text,do_new))
	dp.add_handler(MessageHandler(Filters.text,do_echo))

	dp.add_handler(CallbackQueryHandler(callback=keyboard_callback_handler))
	#dp.add_handler(CallbackQueryHandler(callback=keyboard_callback))
    
	updater.start_polling()
	updater.idle()


	#logger.info("Ending...")

if __name__ == '__main__':
    main()