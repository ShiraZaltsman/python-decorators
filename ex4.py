#Write a decorator that implement a cache mechanism.
#(hint: store your values in a dict and than before calling the function check if you already got an answer)

import time


def ceche_mechanisem(func):
    result=0
    def wrapper(*args, **kwargs):
        nonlocal result
        if(result):
            return func
        result = func(*args, **kwargs)
        return func
    return wrapper

@ceche_mechanisem
def somfanc():
    print("I'm works only one time :)")
    return 1


somfanc()
somfanc()
somfanc()