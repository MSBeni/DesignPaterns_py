# just to check the funny usage of the closures
counter_dict = {}


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counter_dict[fn.__name__] = count
        print(counter_dict)
        print("Function {} is called {} times".format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner


def add(a, b, c):
    return a+b+c


def multiply_(a, b):
    return a*b


counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
print(counter_add(10, 20, 30))
print(counter_add(1, 2, 3))

counter_multiply = counter(multiply_)
print(counter_multiply(10, 20))


