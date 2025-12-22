import logging

# logging sitting
 
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s -%(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()

    ]

)

logger = logging.getLogger("ArithmethicApp")

def add(a, b):
    result=a+b
    logger.debug(f"Addition operation performed: {a} + {b} = {result}")
    return result


def subtract(a, b):
    result=a+b
    logger.debug(f"subtracting operation performed: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result=a+b
    logger.debug(f"Multiplying operation performed: {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result=a+b
        logger.debug(f"Dividing operation performed: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero attempted")
        return None
    
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 0)
divide(10, 2)