class Fruit:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size

    def __str__(self):
        return f"{self.name} is {self.color}"


#inheritence
class Mango(Fruit):
    def __init__(self,name,color,size,variety):
        super().__init__(name,color,size)
        self.variety=variety
if __name__=="__main__":

    f=Fruit('watermelon','green','large')
    print(f)
    m=Mango('mango','yellow','small','safeda')
    print(m)
    m2=Mango('mango','green','large','langada')
    print(m2)
    