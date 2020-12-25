# defining decorator and function


def count(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("The function {} is called {} times".format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner


@count
def add(a, b, c=10):
    return a+b+c


counter_add = count(add)
print(counter_add.__name__)
print(counter_add(10, 20, 30))
