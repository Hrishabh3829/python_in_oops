def greet(fx):
    def mfx(*args,**kwargs):
        #modified fx
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet  #greet-->a decorator function used to modify the function or do-----> greet(hello)()
def hello():
    print("Hello world")

# @greet
def add(a,b):
    print(a+b)
hello()
greet(add)(1,2)
