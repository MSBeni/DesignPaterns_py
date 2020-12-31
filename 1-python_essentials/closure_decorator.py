# defining decorator and function
from functools import wraps


def count(fn):
    cnt = 0
    # @wraps(fn) is equal to inner = wraps(fn)(inner) & equal to inner.__name__ = fn.__name__ inner.__doc__ = fn.__doc__
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
    """
    Add some values
    :param a: int - a number to be added
    :param b: int - a number to be added
    :param c: int - a number to be added
    :return: int - sum of the params
    """
    return a+b+c


print("the memory address of the add func is {}".format(id(add)))
counter_add = count(add)

print(counter_add.__name__)
print("the memory address of the counter_add func is {}".format(id(counter_add)))
print("\n")
print(help(add))
print("\n")
print(counter_add(10, 20, 30))
print("\n")


# Let's add another function
def mult(a, b, c=1, *, d):
    return a*b*c*d


counter_mult = count(mult)
print(counter_mult(2, 4, d=8))















