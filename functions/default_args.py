def add(a,b,c,d): 
    return a+b+c+d

if __name__=="__main__":
    print(add(a=4,b=5,c=6,d=8))


def add(a,b,c=1,d=0):
    return a+b+c+d

if __name__=="__main__":
    out=add(20,20)
    print(out)
    out=add(20,20,20)
    print(out)
    out=add(20,20,10,20)
    print(out)
    out=add(20,20,c=10)
    print(out)
    out=add(20,20,d=20)
    print(out)
    out=add(20,20,d=20,c=10)
    print(out)
    out=add(20,d=20,c=10,b=20)
    print(out)
