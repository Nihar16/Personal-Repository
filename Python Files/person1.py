class Person(object):
        def __init__(self, name="abc", age=20):
                self.name = name
                self.age = age      
        def talk(self):
                print( "Hi, I am", self.name)
        def __str__(self):
                return( "Hi, I am " + self.name+" and I am "+ str(self.age) )

one = Person(name="Yuzhen", age = "forever 20")
print( one)

two = Person()
print (two)
