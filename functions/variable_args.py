# there is an option to make the number of parameters
# flexible in a function
# args is the name of parameters

def multiplier(*numbers):
    out=1 
    for val in numbers:
        out *=val
        return out

print(multiplier(2,3,4,5))
print(multiplier(2,3,4,5,6,7,8,9,10))
print(multiplier())
print(multiplier(3,3))
