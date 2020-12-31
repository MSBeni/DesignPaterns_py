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


@cached
def fib_rec(n):
    print("Calculating fib({}):".format(n))
    return 1 if n < 3 else fib_rec(n-2)+fib_rec(n-1)


print(fib_rec(8))

print(fib_rec(8))

print(fib_rec(30))
print(fib_rec(40))