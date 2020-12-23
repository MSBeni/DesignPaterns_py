"""
def my_func(a: <expression>, b: <expression>) -> <expression>:
pass
"""


def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
    return a * b


print(help(my_func))

# ----------------------------------------------------------------------------------

x = 3
y = 5


def my_func(a: str) -> 'a repeated ' + str(max(x, y)) + ' times':
    return a*max(x, y)


print(help(my_func))