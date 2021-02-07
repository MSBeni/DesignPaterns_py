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


# Now create the Fibonacci in 3 approaches
def rec_fib(n):
    if n <= 2:
        return 1
    else:
        return rec_fib(n-2) + rec_fib(n-1)

@timed
def fibo_calc(n):
    return rec_fib(n)


print(fibo_calc(35))

# another approach
@timed
def fibo_loop(n):
    if n <= 2:
        return 1
    fib1 = 1
    fib2 = 1
    for i in range(3, n+1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


print(fibo_loop(35))
