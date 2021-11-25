class father:
    def __init__(self,prop=0):
        self.property=prop

    def disp(self):
        print ("Father's Property is ",self.property)

class son(father):
    def __init__(self,prop=0,prop1=0):
        super().__init__(prop)
        self.property1=prop1

    def disp(self):
        print ("Child's self Property is ",self.property1)
        print ("Child's total Property is ",self.property+self.property1)
        super().disp()

s=son(20000,80000)
s.disp()
