class ParentClass:
    def __init__(self):
        self.a = 1
        print("Parent Class Object Created")
    def someMethod(self):
        print("Hello")

class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Object Created")

parent = ParentClass()
child = ChildClass()

# Examples
'''
isinstance(parent, ParentClass)
isinstance(5, int) 
isinstance(child, ParentClass)
isinstance(parent, (ParentClass, int)) 
isinstance(parent, ChildClass)

isinstance(parent, MyClass)
try: 
    isinstance(parent, MyClass) 
except NameError: 
    print("No such class")

issubclass(ChildClass, ParentClass) 
issubclass(ParentClass, ParentClass) 
issubclass(ChildClass, int) 
issubclass(ChildClass, (int, ParentClass)) 

hasattr(parent, 'a') 
hasattr(parent, 'someMethod') 
hasattr(parent, 'b')

getattr(parent, 'a')
getattr(parent, 'someMethod')
getattr(parent, 'b', 'Not Found')
setattr(parent, 'a', 2)
'''