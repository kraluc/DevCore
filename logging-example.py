#!/bin/env python

import logging

# Set logging level
logging.basicConfig(level=logging.INFO)

logging.info('This will get logged')
logging.error('This will get logged too')
logging.debug('This will NOT get logged')

def doSomething():
    raise

try:
    doSomething()
except:
    logging.critical('This will be logged in case of an error')