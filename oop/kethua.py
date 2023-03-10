class Name:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getName(self):
        print("name", self.name)
    def getOr(self):
        print( " O ", self.Or)

class D(Name):
     Or = "yes"


    
d = D("RD", 18)

d.getName()
d.getOr()
