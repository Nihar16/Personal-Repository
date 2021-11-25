class a:
    pass
class b:
    pass
class c:
    pass
class x(a,b):
    pass
class y(c):
    pass
class p(x,y):
    pass
ob=p()
print(p.mro())
