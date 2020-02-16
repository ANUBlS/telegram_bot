import logging
import urllib
import json

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,
                      InlineKeyboardMarkup, ParseMode, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, VIET, BIO, FRST, SCND, THRD, FRTH, FFTH, SXT = range(9)
data = []

CALLBACK_BUTTON1 = "callback_button1"
CALLBACK_BUTTON2 = "callback_button2"

TITLES = {
    CALLBACK_BUTTON1: "Buy New Ticket ",
    CALLBACK_BUTTON2: "View Ticket"
    }


def get_back():

	keyboard = [

        [
            InlineKeyboardButton(
                TITLES[CALLBACK_BUTTON1], callback_data=CALLBACK_BUTTON1),
            InlineKeyboardButton(
                TITLES[CALLBACK_BUTTON2], callback_data=CALLBACK_BUTTON2),
        ],
    ]
	return InlineKeyboardMarkup(keyboard)


def keyboard_callback(update, context, chat_data=None, **kwargs):

	query = update.callback_query
	data = query.data

	current_text = update.effective_message.text
	#print(data+'--*'+str(query.data ))
    
	if data == 'callback_button1':
		print('88')
		return new(query,context)
	elif  data=='callback_button2':
		return VIET
    # do_new(bot=bot,update=update)
	# print ('rrr')


def start(update, context):
    reply_keyboard = [['Yes'],['No']]
    
    word =update.message.text
    
    if (word.find('Buy') != -1):
        print (update.message.text)
        update.message.reply_text(
        'Hi again! want to buy new ticket? ' ,
         reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True)
       )
        #return BIO
    else:
        update.message.reply_text(
            'Hi! Do yo want to play Lottery ? '
            'Click YES Otherwise  choose NO.\n\n'
            ,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return GENDER

def new(update, context):

    reply_keyboard = [['Buy Tickets'],['View Ticket']]
    
    user = update.message.from_user
    elem_to_find = update.message.text
    update.message.reply_text('I see you want to play! Buy ticket or View your Tickets bought for this round  , ',
                                reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return GENDER
    
        


def gender(update, context):

    reply_keyboard = [['Buy Tickets'],['View Ticket']]
    print('t55')
    if update.message.text=='Yes':
        user = update.message.from_user
        elem_to_find = update.message.text
        update.message.reply_text('I see you want to play! Buy ticket or View your Tickets bought for this round  , ',
                                reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

        return BIO
    else:
        return cancel(update, context)
        



def bio(update, context):
    reply_keyboard = [['1', '2','3','4','5','6',],[ '7','8','9','10','11', '12',],['13','14','15','16', '17','18',],['19','20','21', '22','23','24','25']]
    user = update.message.from_user
    
    # logger.info("USer id %s: %s", update.message.text,context.user_data)
    if update.message.text=='Buy Tickets':
        update.message.reply_text('Choose 1ST numbers .',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))
        context.user_data[FRST]=update.message.text
        return FRST

def First(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25']    ]
    user = update.message.from_user
   
    context.user_data[SCND]=update.message.text
   
    elem_to_find = context.user_data[FRST]
    elem_to_find2 = context.user_data[SCND]

    # res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]  


    # logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Choose 2 number',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return SCND

def Second(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25']
                       ]
    user = update.message.from_user
    context.user_data[THRD]=(update.message.text)
    # elem_to_find = update.message.text

    elem_to_find = context.user_data[FRST]
    elem_to_find2 = context.user_data[SCND]
    elem_to_find3 = context.user_data[THRD]


    # res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find] 
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find3] 
    

    # logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Choose 3 number.',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return THRD

def Third(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25']
                        ]
    user = update.message.from_user
    context.user_data[FRTH]=(update.message.text)

    elem_to_find = update.message.text

    elem_to_find  = context.user_data[FRST]
    elem_to_find2 = context.user_data[SCND]
    elem_to_find3 = context.user_data[THRD]
    elem_to_find4 = context.user_data[FRTH]
   

    # res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find3]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find4]   
    

    # logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Choose 4 number',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return FRTH

def Fourth(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25'] ]
    user = update.message.from_user
    context.user_data[FFTH]=(update.message.text)

    elem_to_find5 = update.message.text

    elem_to_find = context.user_data[FRTH]
    elem_to_find2 = context.user_data[FRST]
    elem_to_find3 = context.user_data[SCND]
    elem_to_find4 = context.user_data[THRD]
   
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find3]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find4]  
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find5] 

   
    # logger.info("Gender of %s: %s", user.first_name, context.user_data)
    update.message.reply_text('Choose your last number .',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return FFTH

def Fifth(update, context):

    reply_keyboard = [['view Ticket']]
    user = update.message.from_user
    context.user_data[SXT]=(update.message.text)
    elem_to_find = update.message.text

    elem_to_find = context.user_data[FRTH]
    elem_to_find2 = context.user_data[FRST]
    elem_to_find3 = context.user_data[SCND]
    elem_to_find4 = context.user_data[THRD]
    elem_to_find5 = context.user_data[FFTH]
    # res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find3]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find4]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find5]  
  

    logger.info("Choosed numbers %s: %s", user.first_name,context.user_data)
    update.message.reply_text('You choosed this numbers  \n\n'

                              + elem_to_find2+'-'+elem_to_find3+'-'+elem_to_find4+'-'+elem_to_find+'-'+elem_to_find5 +'- '+update.message.text
                              ,#reply_markup=get_back()
                                reply_markup=ReplyKeyboardRemove()
                              )
    update.message.reply_text( 'press "/start" to buy a new ticket ,to view your bought tickets press "View Ticket" ')

    return ConversationHandler.END

def viet(update, context):
   # reply_keyboard = [['Buy New ticket'] ]

    elem_to_find = context.user_data[SXT]
    elem_to_find =  context.user_data[FRTH]
    elem_to_find2 = context.user_data[FRST]
    elem_to_find3 = context.user_data[SCND]
    elem_to_find4 = context.user_data[THRD]
    elem_to_find5 = context.user_data[FFTH]
    user = update.message.from_user
    print (context.user_data)
    #logger.info("ended vie ticked cli", context.user_data)
    update.message.reply_text(elem_to_find2+'-'+elem_to_find3+'-'+elem_to_find4+'-'+elem_to_find+'-'+elem_to_find5 +'- '+elem_to_find, )

    return ConversationHandler.END




def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the .", user.first_name)
    update.message.reply_text('Bye! I hope we can play again some day .\n\n'
                                'If you want to start over press /start ',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("984290476:AAE4kpNCJ1ll6FSQyNHGb79dl1FovKI2w2o", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),CommandHandler('new', new)],
        

        states={
            GENDER:[MessageHandler(Filters.text, gender)],
            BIO:[MessageHandler(Filters.text, bio)],
            FRST:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), First)],
            SCND:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Second)],
            THRD:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Third)],
            FRTH:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Fourth)],
            FFTH:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Fifth)]

            
           # PHOTO: [MessageHandler(Filters.photo, photo),CommandHandler('skip', skip_photo)],

           # LOCATION: [MessageHandler(Filters.location, location),CommandHandler('skip', skip_location)],

            
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('view',viet))
    dp.add_handler(CallbackQueryHandler(callback=keyboard_callback))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    print('7777')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
