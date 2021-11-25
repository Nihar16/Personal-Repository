class Critter(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print( "Hi. I'm", self.name, "\n")
    

crit1 = Critter("abcd")
print(crit1.name)
crit1.talk()


