#learning getter setters in python
class Myclass:
    def __init__(self,value):
        self.value=value
@property
def value(self):
    return self.value
obj=Myclass(10)