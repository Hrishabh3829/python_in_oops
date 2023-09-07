class Resume:
    name="Hrishabh"
    age=20
    networth="700"
    occupation="software developer"

    def info(self):
        print(f"{self.name} age is {self.age} whose networth is {self.networth} works as {self.occupation}")
              
b=Resume()
a=Resume()
c=Resume()


b.name="Gaurav"
b.age=19
b.networth="983222"
b.occupation="Accountant"
# print(a.name,a.age,a.networth,a.occupation)
c.name="Mithesh"
c.age=20
c.networth="83923"
c.occupation="HR"

a.info()    
b.info()    
c.info()