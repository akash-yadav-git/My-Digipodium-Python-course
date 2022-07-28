numbers=list(map(int,input('>>').split()))
print(numbers)

numbers_halfed =list(map(lambda i: int(i)/2,input('>>'.split())))
print(numbers_halfed)

x=[12,15,19,17,13,20]
xodd=list(filter(lambda i:i%2!=0,x))
print(xodd)
