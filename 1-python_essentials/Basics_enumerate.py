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
lambda_test = lambda x, *args, y, **kwargs: (x+10, args, y+5, kwargs)

print(lambda_test(1, 'a', 12, 24, a=50, y=20, b='sss'))
print('\n')
print(lambda_test(1, 'a', 12, y=24, a=50, c=20, b='sss'))