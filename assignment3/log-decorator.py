# Task 1

# setting up logging
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


# logs the name, positional arguments, keyword arguments and the value the function returns
# to a file decorator.log
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args or 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs or 'none'}")
        logger.log(logging.INFO, f"return value: {func(*args, **kwargs)}")

    return wrapper


# function with no arguments
@logger_decorator
def hello():
    print("hello")


# function with positional arguments only
@logger_decorator
def hello_args(*args):
    print("hello")


# function with keyword arguments only
@logger_decorator
def hello_kwargs(**kwargs):
    print("hello")


hello()
hello_args(1, 2, 3)
hello_kwargs(name="Janet", role="Developer")
