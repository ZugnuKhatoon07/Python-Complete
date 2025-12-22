from logger import logging

def add(a, b):
    logging.debug("The addtion operation is taking place")
    return a + b

logging.debug("Starting the addition operation")
add( 10, 15 )