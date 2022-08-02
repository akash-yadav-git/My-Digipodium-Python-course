# generators are special functions in python
#that can be used to generate a sequence of values
# insted of returning the value from a function once
#we put the value into a memory space using the yield keword
#and then we can use next()function to get next value

from re import A


def cube(limit):
    for i in range (1,limit+1):
        yield i**3

def fib(limit):
    a,b=0,1
    for i in range(limit):
     yield a
     a,b=b,a+b

for c in cube(10):
    print(c)

for f in fib(15):
    print(f, end='|')


def square(limit):
    for i in range(1,limit+1):
        yield

