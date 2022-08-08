class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


if __name__=="__main__":
    p=Person('Raju',38)
    p2=Person('Vijay',30)
    p3=Person('Sanju',30)

    if p>p3:
        print(f'{p.name} is elder')
    person_list=[p,p2,p3]
    person_list.sort()
    print(person_list)
    