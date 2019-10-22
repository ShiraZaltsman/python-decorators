import inspect


def dump_args(func):
    """Decorator to print function call details - parameters names and effective values."""
    def wrapper(*args, **kwargs):
        func_args = inspect.signature(func).bind(*args, **kwargs).arguments
        func_args_str =', '.join('{} = {!r}'.format(*item) for item in func_args.items())
        print(f'{func.__qualname__} ( {func_args_str} )')
        return func(*args, **kwargs)
    return wrapper


@dump_args
def test(a, b=4, c='blah-blah', *args, **kwargs):
    return a+b


ans = test(1)
test(7, 19)
test(1, d=5)
test(9, 2, "Hello World", 4, 5, d=6, g=12.9)

print(ans)