class Dec:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        return "The values are {}, {}, and {}".format(self.a, self.b, args)


obj = Dec(10, 20)
print(obj(5))


########################################################################################################################
# decorative class approach
class Dec2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("The values are {}, {}".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner


@Dec2(10, 20)
def smp_prt(msg):
    return "hello {}".format(msg)


print(smp_prt("world"))