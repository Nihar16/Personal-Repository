class Person:
    def __init__(self):
        self.name="Anuja"
        self.db=self.Dob()  #db=inner class object

    def display(self):
        print("Name\t:",self.name)

    #Inner class
    class Dob:
        def __init__(self):
            self.dd=input("date: ")
            self.mm=1
            self.yy=19

        def display(self):
            print("DOB\t:",self.dd,"/",self.mm,"/",self.yy)

p=Person()
p.display()
x=p.db
x.display()

y=Person().Dob()
y.display()
print(y.yy)

print(y.dd)
