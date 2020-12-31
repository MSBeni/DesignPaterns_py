def timed(n):
    def dec_in(fn):
        from functools import wraps
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            calc_time = 0
            for t in range(n):
                start = perf_counter()
                result = fn(*args, **kwargs)
                calc_time += perf_counter() - start
            print("{0} is calculated in {1:.6f}".format(fn.__name__, calc_time / n))
            return result
        return inner
    return dec_in


def cached(fn):
    from functools import wraps
    mem = dict()
    @wraps(fn)
    def inner(n):
        # nonlocal mem
        if n not in mem:
            mem[n] = fn(n)
        return mem[n]
    return inner


@timed(10)
@cached
def fib_rec(n):
    # print("Calculating fib({}):".format(n))
    return 1 if n < 3 else fib_rec(n-2)+fib_rec(n-1)


print(fib_rec(15))
print("\n")
print(fib_rec(18))



@cached
def fib_rec2(n):
    # print("Calculating fib({}):".format(n))
    return 1 if n < 3 else fib_rec(n-2)+fib_rec(n-1)


print(fib_rec(15))
print("\n")
print(fib_rec(18))


@timed(10)
def fibo_calc(n):
    return fib_rec2(n)


print(fibo_calc(15))
print("\n")
print(fibo_calc(18))