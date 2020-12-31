def logged(fn):
    from functools import wraps
    from datetime import datetime

    @wraps(fn)
    def inner(*args, **kwargs):
        now = datetime.now()
        result = fn(*args, **kwargs)
        print("{0}: called {1}".format(now, fn.__name__))
        return result
    return inner


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed_time = end - start

        args_val = [str(argum) for argum in args]
        kwargs_keyval = ['{0} = {1}'.format(k, v) for (k, v) in kwargs.items()]
        args_val.extend(kwargs_keyval)
        all_args = ','.join(el for el in args_val)
        print('function {1}({2}) is calculated in {0:.6f} sec.'.format(elapsed_time, fn.__name__, all_args))

        return result

    return inner

# Test the logger
@logged
def func1():
    pass


@logged
@timed
def factoriel(n):
    from functools import reduce
    from operator import mul

    return reduce(mul, range(1, n+1))


print(factoriel(50))