class Father:
    def height(self):
        print("Height is 6 ft")

class Mother:
    def color(self):
        print("Eyes are brown")

class child(Father,Mother):
    pass

c=child()
print("The child has inherited")
c.height()
c.color()
