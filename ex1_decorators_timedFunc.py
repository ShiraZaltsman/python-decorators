import time


def timeit(method):
    def timed():
        ts = time.time()
        result = method()
        te = time.time()
        print("time: ")

        print(str((te - ts) *1000)+" milliseconds")

    return timed

@timeit
def somfanc():
    for i in range(9000000):
        b = []
    return 0

somfanc()

