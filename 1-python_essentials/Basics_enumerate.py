# Simply practice the python essentials
s = 'hello'

for index, char in enumerate(s):
    print(index, char)

print('\n')
# ____________________________________________________________
lst_ = ['a', 'b', 'c']

for index_, c in enumerate(lst_):
    print(index_, c)


# ------------------------------------------------------------
lam_test = lambda x, *args, y, **kwargs: (x+10, args, y+5, kwargs)

print(lam_test(1, 'a', 12, 24, a=50, y=20, b='sss'))
print('\n')
print(lam_test(1, 'a', 12, y=24, a=50, c=20, b='sss'))
print('\n')


# ------------------------------------------------------------
def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)


print(apply_func(lambda x, y: x**y, 10, 20))