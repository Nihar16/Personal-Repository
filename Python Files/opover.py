class corepython:
    def __init__(self,pages):
        self.pages=pages
    def __gt__(self, abcd):
        return self.pages>abcd.pages

class pythonProg:
    def __init__(self,pages):
        self.pages=pages

b1=corepython(750)
b2=pythonProg(500)
if b1>b2:
    print ("Core Python has more pages")
else:
    print ("Python programming has more pages")
