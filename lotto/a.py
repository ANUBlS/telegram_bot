import logging
import urllib
import json

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, VIET, BIO,FRST ,SCND,THRD,FRTH,FFTH,SXT = range(9)
data=[]


def start(update, context):
    reply_keyboard = [['1ee', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25'],
                      ['view Ticket']   ]

                 
    update.message.reply_text(
        'Hi! My name is Professor Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'Are you a boy or a girl?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return GENDER

def gender(update, context):

    reply_keyboard = [['BUY'],['view Ticket']   ]
    user = update.message.from_user

    elem_to_find = update.message.text
# print (update.message.text)
   
        

    #res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    

   # logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('I see! Please send me a photo of yourself, '
                              'so I knovvvw what you look like, or send /skip22 if you don\'t want to.',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return BIO



def bio(update, context):
    reply_keyboard = [['1', '2','3','4','5','6',],[ '7','8','9','10','11', '12',],['13','14','15','16', '17','18',],['19','20','21', '22','23','24','25'],['view Ticket']   ]
    user = update.message.from_user
    
    #logger.info("USer id %s: %s", update.message.text,context.user_data)
    
    update.message.reply_text('Choose numbers .',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))
    context.user_data[FRST]=update.message.text
    return FRST

def First(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25'],
                      ['view Ticket']   ]
    user = update.message.from_user
   
    context.user_data[SCND]=update.message.text
   
    elem_to_find = context.user_data[FRST]
    elem_to_find2 = context.user_data[SCND]

    #res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]  


    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Choose 2 number',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return SCND

def Second(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25'],
                      ['view Ticket']   ]
    user = update.message.from_user
    context.user_data[THRD]=(update.message.text)
    #elem_to_find = update.message.text

    elem_to_find = context.user_data[FRST]
    elem_to_find2 = context.user_data[SCND]
    elem_to_find3 = context.user_data[THRD]


    #res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find] 
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find3] 
    

    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Choose 3 number.',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return THRD

def Third(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25'],
                      ['view Ticket']   ]
    user = update.message.from_user
    context.user_data[FRTH]=(update.message.text)

    elem_to_find = update.message.text

    elem_to_find  = context.user_data[FRST]
    elem_to_find2 = context.user_data[SCND]
    elem_to_find3 = context.user_data[THRD]
    elem_to_find4 = context.user_data[FRTH]
   

    #res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find2]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find3]
    for sub in reply_keyboard: 
        sub[:] = [ele for ele in sub if ele != elem_to_find4]   
    

    #logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Choose 4 number',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return FRTH

def Fourth(update, context):

    reply_keyboard = [['1', '2','3','4','5','6',],
                      [ '7','8','9','10','11', '12',],
                      ['13','14','15','16', '17','18',],
                      ['19','20','21', '22','23','24','25'],
                      ['view Ticket']   ]
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

   
    #logger.info("Gender of %s: %s", user.first_name, context.user_data)
    update.message.reply_text('WGBsrdfg .',
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
    #res = [[ele for ele in sub if ele != elem_to_find] for sub in reply_keyboard]
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
  

    logger.info("Gender rrrr %s: %s", user.first_name,context.user_data)
    update.message.reply_text('I seeENDED',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    return viet

def viet(update, context):
    reply_keyboard = [['view Ticket'] ]
    user = update.message.from_user
    print (context.user_data)
    logger.info("ended vie ticked cli", context.user_data)
    update.message.reply_text('Bye! I asas we can talk again some day.',
                               reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=True))

    #return ConversationHandler.END



def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
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
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER:[MessageHandler(Filters.text, gender)],
            BIO:[MessageHandler(Filters.text, bio)],
            FRST:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), First)],
            SCND:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Second)],
            THRD:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Third)],
            FRTH:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Fourth)],
            FFTH:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), Fifth)],
            VIET:[MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25)$'), viet)]
           # PHOTO: [MessageHandler(Filters.photo, photo),CommandHandler('skip', skip_photo)],

           # LOCATION: [MessageHandler(Filters.location, location),CommandHandler('skip', skip_location)],

            
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

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


