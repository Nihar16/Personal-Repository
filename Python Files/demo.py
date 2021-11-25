class Abc:
    c=3   #class variable
    def __init__(self):
        self.a=1
        Abc.b=2     #to define class variable inside instance method, use classname

    def ghi(self):    #instance method
        print(self.a)
        self.b=5     #instance copy of class variable-->instance name space
        print(self.b)   #calls class variable from instance namespace
        print(Abc.b)   #calls class variable from class namespace (Truly common)
        print(Abc.c)

    @classmethod
    def abcd(cls):
        #print(self.a)   can NOT call instance variables
        print(Abc.b)     # can call class variables either using cls or classname
        print(cls.c)

    @staticmethod
    def defg():
        #print(self.a)    can NOT call instance variables
        print(Abc.b)   # cannot use cls parameter
        print(Abc.c)

ab=Abc()
print(ab.a)
print(ab.b)
print(Abc.c)
ab.ghi()
ab.abcd()
Abc.abcd()  #can NOT call class methods using classname unless decorator is used
ab.defg()
Abc.defg()

