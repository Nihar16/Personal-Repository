class Puppy(object):
    def __init__(self):
        self.name = []
        self.color = []

    def __setitem__(self, name, color):
        self.name.append(name)
        self.color.append(color)

    def __getitem__(self, name):
        if name in self.name:
             return self.color[self.name.index(name)]
        else:
             return None

dog = Puppy()
dog['Max'] = 'brown'
dog['Ruby'] = 'yellow'
print ("Max is", dog['Max'])
print("puppy is ", dog['puppy'])
