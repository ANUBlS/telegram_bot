import logging.config




LOGGING = {
    'disable_existing_logger':True,
    'version':1,
    'formatter':{
            'verbose':{
            'format':'%(levelname)s %(module)s.%(funcname)s | %(asctime)s | %(message)s',
            'datefmt':'%Y-%m-%d %H-:%M:%S',
            },
    },
    'handlers':{
        'console':{
            'class':'logging.Streamhandler',
            'level':'DEBUG',
            'formatter':'verbose',
        },
    },

    'loggers':{
    '':{
        'handlers':['console'],
        'level':'INFO',
        'propogate':False,
    },
 },


}


logging.config.dictConfig(LOGGING)