class A:
    @classmethod
    def ab(cls):
        print("this works")
    def __init__(self):
        A.ab()
aa=A()
