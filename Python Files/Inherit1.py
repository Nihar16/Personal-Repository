class Teacher:
    def setname(self,nob):
        self.name=nob
    def getname(self):
        return self.name
    def setsalary(self,sob):
        self.salary=sob
    def getsalary(self):
        return self.salary

class Student(Teacher):
    def setmarks(self,mob):
        self.marks=mob
    def getmarks(self):
        return self.marks

s=Student()
s.setname("Name")
s.setmarks(100)
print("Hello {}, You have got {} marks".format(s.name,s.getmarks()))
