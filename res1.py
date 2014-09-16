"""
 ***************************
            Course 1
 ****************************
"""

"""
 JavaXPython
"""
# User Input
i = input("Enter your name : ")
print("Hello "+i)


# Class example
class myClass (object) :
    # Static attribute
    sattr = " "
    # Constructor ( self <= > this in Java )
    def __init__ ( self ) :
        # Instance attribute
        self . attr1 = " "
        
    # Static method
    @staticmethod
    def foo ( arg1 , arg2) :
        pass
    
    # Class method
    @classmethod
    def foo ( cls , arg2) :
        pass

"""
 Tricks
"""
#Unpacking
a,b,c = 1,2,3
a,b = b,a
a,*b,c = [1,2,3,4,5]

#List slices
a = [0,1,2,3,4,5,6,7,8,9,10]
a[2:5]
a[2::5]
a[::2]
a[::-1]
a[2:3] = [0, 0]

#Zipping
a = [1,2,3]
b = ['a','b','c']
z = zip(a, b)

#Generators
g = (x ** 2 for x in range(10)) # list
next(g)
g = {x ** 2 for x in range(10)} # Sets
g


"""
 Decorators
"""
def printerDecorator(function):
    def printer():
        print("Before calling {0}".format(function))
        function()
        print("After calling {0}".format(function))
    return printer

@printerDecorator
def foo():
    print("Hello world !")

foo()


"""
 exec
"""
def foo():
    print ( " hello " )
foo ()


exec( "def foo():\
    print (\" hello \")")
foo()


"""
 MetaClass
"""
class Person () :
    # Constructor
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
toto = Person("toto", 20)
print(toto.name+" "+str(toto.age))


class metaPerson(type):
    # Constructor
    def __init__(cls, name, bases, methods):
        print("Class initialisation")
        return type.__init__(cls, name, bases, methods)

    # Create the object
    def __new__(self, name, bases, methods):
        print("Class creation")
        # Static attribute
        self.num = 1
        return type.__new__(self, name, bases, methods)

class Person(metaclass=metaPerson):
    # Constructor
    def __init__(self, name, age):
        self.name = name

toto = Person("toto", 20)



