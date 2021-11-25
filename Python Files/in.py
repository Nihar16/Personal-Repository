class father:
    def __init__(self):
        self.a=10

class son(father):
    def __init__(self):
        super().__init__()
        self.a=5
        
s=son()
print(s.a)
