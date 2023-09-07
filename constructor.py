#learning constructor
class Person:
    name="Hrishabh"
    occ="Developer"

    def __init__(self,name,occ):#self parameter is automatically assigning or it is a person 
        print("Hey im a person")    #this object is invoking whenever we create or update values for person
        self.name=name
        self.occ=occ 


    def info(self):
        print(f"{self.name} is {self.occ}")
a=Person("Hrishabh","Developer")
b=Person("Anushka","HR")
c=Person(1,2)
# b.name="Anushka"
# b.occ="HR"
a.info()
b.info()
c.info()