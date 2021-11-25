class Teacher:
    def __init__(self,nob,sob=0):
        self.name=nob
        self.salary=sob
    def getname(self):
        return self.name   
    def getsalary(self):
        return self.salary

class Student(Teacher):
    """def __init__(self,nob,mob=0):
        self.name=nob
        self.marks=mob"""
    def setmarks(self,mob):
        self.marks=mob
    def getmarks(self):
        return self.marks
p=Teacher("Name")
s=Student("Name")
s.setmarks(100)
print("Hello {}, You have got {} marks".format(p.getname(),p.getsalary()))
print("Hello {}, You have got {} marks".format(s.getname(),s.getmarks()))
        
