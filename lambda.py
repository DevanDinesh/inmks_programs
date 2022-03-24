# x=lambda a,b  :a+b
# print(x(2,5))

# x=lambda a : a+30
# print(x(20))


def fun(n):
    return lambda b:b+n
x=fun(2)
print(x(8))