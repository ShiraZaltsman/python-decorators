import time


def slow_func(method):
    def slow():
        time.sleep(1)
        result = method()
    return slow

@slow_func
def somfanc():
    print("I'm late in one second :(")
    return 0

somfanc()