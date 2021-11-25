class student:
    def __init__(self,roll,name,age):
        self.roll=roll
        self.name=name
        self.age=age
    def display(self):
        print("{:5d}{:20s}{:10.2f}".format(self.roll,self.name,self.age))
