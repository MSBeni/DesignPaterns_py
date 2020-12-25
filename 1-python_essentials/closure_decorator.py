# defining decorator and function
from functools import wraps


def count(fn):
    cnt = 0

    # @wraps(fn) is equal to inner = wraps(fn)(inner)
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("The function {} is called {} times".format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    # inner.__name__ = fn.__name__
    # inner.__doc__ = fn.__doc__
    # inner = wraps(fn)(inner)
    return inner


@count
def add(a, b, c=10):
    return a+b+c


counter_add = count(add)
print(counter_add.__name__)
print(counter_add(10, 20, 30))
