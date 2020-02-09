from telegram.ext import Updater, InlineQueryHandler, CommandHandler,Filters,MessageHandler,CallbackQueryHandler
from subprocess import Popen,PIPE


from telegram import InlineKeyboardButton,ParseMode, InlineKeyboardMarkup,ReplyKeyboardRemove,ReplyKeyboardMarkup
import requests
import re
import datetime
import logging

import importlib
import os
import sys



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



logger = logging.getLogger()
logger.setLevel(logging.INFO)





CALLBACK_BUTTON1 = "callback_button1"
CALLBACK_BUTTON2 = "callback_button2"
CALLBACK_BUTTON3 = "callback_button3"
CALLBACK_BUTTON4 = "callback_button4"
CALLBACK_BUTTON5 = "callback_button5"
CALLBACK_BUTTON6 = "callback_button6"
CALLBACK_BUTTON7 = "callback_button7"
CALLBACK_BUTTON8 = "callback_button8"
CALLBACK_BUTTON9  = "callback_button9"
CALLBACK_BUTTON10 = "callback_button10"
CALLBACK_BUTTON11 = "callback_button11"
CALLBACK_BUTTON12 = "callback_button12"
CALLBACK_BUTTON13 = "callback_button13"
CALLBACK_BUTTON14 = "callback_button14"
CALLBACK_BUTTON15 = "callback_button15"
CALLBACK_BUTTON16 = "callback_button16"
CALLBACK_BUTTON17 = "callback_button17"
CALLBACK_BUTTON18 = "callback_button18"
CALLBACK_BUTTON19  = "callback_button19"
CALLBACK_BUTTON20 = "callback_button20"
CALLBACK_BUTTON21 = "callback_button21"
CALLBACK_BUTTON22 = "callback_button22"
CALLBACK_BUTTON23 = "callback_button23"
CALLBACK_BUTTON24 = "callback_button24"
CALLBACK_BUTTON25  = "callback_button25"
CALLBACK_BACK_BTN  = "call_back_btn"



TITLES = {
    CALLBACK_BUTTON1: "1 ",
    CALLBACK_BUTTON2: "2 ",
    CALLBACK_BUTTON3: "3 ",
    CALLBACK_BUTTON4: "4 ",
    CALLBACK_BUTTON5: "5 ",
    CALLBACK_BUTTON6: "6 ",
    CALLBACK_BUTTON7: "7 ",
    CALLBACK_BUTTON8: "8 ",
    CALLBACK_BUTTON9: "9 ",
    CALLBACK_BUTTON10: "10 ",
    CALLBACK_BUTTON11: "11 ",
    CALLBACK_BUTTON12: "12 ",
    CALLBACK_BUTTON13: "13 ",
    CALLBACK_BUTTON14: "14 ",
    CALLBACK_BUTTON15: "15 ",
    CALLBACK_BUTTON16: "16 ",
    CALLBACK_BUTTON17: "17 ",
    CALLBACK_BUTTON18: "18 ",
    CALLBACK_BUTTON19: "19 ",
    CALLBACK_BUTTON20: "20 ",
    CALLBACK_BUTTON21: "21 ",
    CALLBACK_BUTTON22: "22 ",
    CALLBACK_BUTTON23: "23 ",
    CALLBACK_BUTTON24: "24 ",
    CALLBACK_BUTTON25: "25 ",

    CALLBACK_BACK_BTN :"Back"

}




def get_base_inline_keyboard():
	#@print('hhh')
  
	keyboard = [
	[
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1], callback_data=CALLBACK_BUTTON1),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2], callback_data=CALLBACK_BUTTON2),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3], callback_data=CALLBACK_BUTTON3),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4], callback_data=CALLBACK_BUTTON4),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5], callback_data=CALLBACK_BUTTON5),
            
        ],
        [	InlineKeyboardButton(TITLES[CALLBACK_BUTTON6], callback_data=CALLBACK_BUTTON6),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7], callback_data=CALLBACK_BUTTON7),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8], callback_data=CALLBACK_BUTTON8),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON9], callback_data=CALLBACK_BUTTON9),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON10], callback_data=CALLBACK_BUTTON10),

        ],
        [	InlineKeyboardButton(TITLES[CALLBACK_BUTTON11], callback_data=CALLBACK_BUTTON11),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON12], callback_data=CALLBACK_BUTTON12),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON13], callback_data=CALLBACK_BUTTON13),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON14], callback_data=CALLBACK_BUTTON14),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON15], callback_data=CALLBACK_BUTTON15),

        ],

		[	InlineKeyboardButton(TITLES[CALLBACK_BUTTON16], callback_data=CALLBACK_BUTTON16),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON17], callback_data=CALLBACK_BUTTON17),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON18], callback_data=CALLBACK_BUTTON18),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON19], callback_data=CALLBACK_BUTTON19),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON20], callback_data=CALLBACK_BUTTON20),

        ],
        [	InlineKeyboardButton(TITLES[CALLBACK_BUTTON21], callback_data=CALLBACK_BUTTON21),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON22], callback_data=CALLBACK_BUTTON22),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON23], callback_data=CALLBACK_BUTTON23),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON24], callback_data=CALLBACK_BUTTON24),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON25], callback_data=CALLBACK_BUTTON25),

        ],



   
        
    ]
	#print('eeeeee')
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
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON5], callback_data=CALLBACK_BUTTON5),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON6], callback_data=CALLBACK_BUTTON6),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON7], callback_data=CALLBACK_BUTTON7),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON8], callback_data=CALLBACK_BUTTON8),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4], callback_data=CALLBACK_BUTTON4),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_callback(bot, update,chat_data=None,**kwargs):

	query = update.callback_query
	data = query.data
	# now = datetime.datetime.now()
	# chat_id = update.effective_message.chat_id
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

btns=[]
def appending(appdata,chatid, update,bot):
	chats  = update.message.chat_id

	if chatid==chats:		
		if appdata!='ty':
			if len(btns)>=5:
				bot.send_message(chat_id=chats,text="you selected  this numbers= "+str(btns))
				bot.send_message(chat_id=chats,text="Send above numbers to yhis address = ")

			else:

				btns.append([appdata])
			print(btns)

	return btns




def keyboard_callback_handler(bot, update,chat_data=None,**kwargs):

	query = update.callback_query
	data = query.data
	#user=query.from_user
	now = datetime.datetime.now()
	#urrenttext=''
	
	
	print (now)
	chat_id = update.effective_message.chat_id
	current_text = update.effective_message.text

	#appending('ty',chat_id,query,bot)
	

	if data == CALLBACK_BUTTON1:
		
		#appending(TITLES[CALLBACK_BUTTON1],chat_id,query,bot)
		currenttext=current_text+'*'+TITLES[CALLBACK_BUTTON1]
		print (currenttext)
		
		query.edit_message_text(
            text=current_text,
            parse_mode=ParseMode.MARKDOWN,
        )
  
		bot.send_message(
            chat_id=chat_id,
            text="new mess\n\ncallback_query.data={}".format(data),
            reply_markup=get_base_inline_keyboard(),
        )
	elif data == CALLBACK_BUTTON2:
		currenttext=current_text+'*'+TITLES[CALLBACK_BUTTON2]
		print (currenttext)
		#print(chat_id)
		#bot.send_message(chat_id=chat_id,text="pjkjk ",)
		#bot.send_photo(chat_id=chat_id, photo=url)
		return start(bot=bot,update=query)
		


	elif data == CALLBACK_BACK_BTN:
		#print(CALLBACK_BACK_BTN)
		bot.send_message(chat_id=chat_id,text="back ",)
		#bot.send_photo(chat_id=chat_id, photo=url)
		return start(bot=bot,update=query)
		#print('5555')

		


	elif data == CALLBACK_BUTTON3:
		
			
		currenttext=current_text+'*'+TITLES[CALLBACK_BUTTON3]
		print (currenttext)
		query.edit_message_text(
            	text=current_text,
            	reply_markup=get_keyboard2(),
        	)
	elif data == CALLBACK_BUTTON4:
		currenttext=current_text+'*'+TITLES[CALLBACK_BUTTON4]
		print (currenttext)
		print(data)

		query.edit_message_text(
            text=current_text,
            reply_markup=get_base_inline_keyboard(),
        )
	elif data == CALLBACK_BUTTON5:
		#appending(TITLES[CALLBACK_BUTTON5],chat_id,query,bot)
		print(data)

		text = "*exact time  *\n\n{}".format(now)
		query.edit_message_text(
            text=text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard2(),
        )
	elif data in (CALLBACK_BUTTON6, CALLBACK_BUTTON7, CALLBACK_BUTTON8):
		pair = {
            CALLBACK_BUTTON6: "USD-BTC",
            CALLBACK_BUTTON7: "USD-LTC",
            CALLBACK_BUTTON8: "USD-ETH",
        }[data]
		print (pair)

		# try:
		# 	current_price = client.get_last_price(pair=pair)
		# 	text = "* kurs:*\n\n*{}* = {}$".format(pair)
		# #except BittrexError:
		# 	text = "error  :(\n happebed "
		# 	query.edit_message_text(
        #     text=text,
        #     parse_mode=ParseMode.MARKDOWN,
        #     reply_markup=get_keyboard2(),
        # )
	elif data == CALLBACK_BUTTON9:
		#btns.append ([TITLES[CALLBACK_BUTTON9]])

		


		bot.send_message(
            chat_id=chat_id,
            text="press  /start to return buttons ",
            reply_markup=ReplyKeyboardRemove(),
        )









def start(bot, update):
	# custom_keyboard = [['🔴Red Team🔴', '🔵Blue Team🔵'], 
 #                   ['ddd']]
	custom_keyboard =[['1', '2','3','4','5','6',],
 					  [ '7','8','9','10','11', '12',],
 					  ['13','14','15','16', '17','18',],
 					  ['19','20','21', '22','23','24','25'],
 					  ['view Ticket']	]
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
    #text=update.message.text
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
	#return appending('new')
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