# to pass named args in a function we hv another way ie keyword args
# kwargs is the name of parameters and ** before
# it can accept any number of named values in function

def student_report(**kwargs):
    total=0
    for k,v in kwargs.items():
        print(k,v)
        total +=v
    return len(kwargs), total/len(kwargs)


# ex call
print(student_report(rohan=50,akash=90,alka=40))
print(student_report(rohan=50,akash=90,anup=20,vijay=20,lala=40))

