class father:
    def __init__(self):
        self.property=80000

    def disp(self):
        print ("Father's Property is ",self.property)

class son(father):
    def __init__(self):
        self.property=20000

    def disp(self):
        print ("Child's Property is ",self.property)

s=son()
s.disp()
father().disp()
