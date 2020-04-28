# function declaration
c = 0


def add(a, b):
    c = a + b
    return c


# calling the function

s = add(10, 44)

print(f"the sum is {s}")

d = add("hello", "world")
print(d)

# lambda function
v = lambda a: a + 10  # as a=3 means a=3+10=13 where v is a lambda function
print(v(3))  # a=3

d = lambda a: a >= 10

dd = d(2)
print(dd)


# function vs lambda

def mul(x, y):
    print(x * y)
mul(2,3)

aa = lambda q, r: q * r

print(aa(2, 3))


