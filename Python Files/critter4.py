class Critter(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print( "Hi. I'm", self.name, "\n")
    def __str__(self):
            rep = "Critter object\n"
            rep += "name: " + self.name + "\n"
            return rep


crit1 = Critter("ancgfhd")
print(crit1.name)
crit1.talk()
print(crit1)

