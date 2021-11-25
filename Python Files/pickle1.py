import pickle
class Human:
    def __init__(self):
        self.name=input("Enter your name : ")
        self.age=input("Enter your age : ")
    def disp(self):
        print("Hello {}, You are {} year old!".format(self.name,self.age))

with open("Human.dat", "wb") as f:
    insaan=Human()
    pickle.dump(insaan,f)

#f.seek(0,0)
with open("Human.dat", "rb") as f:
    try:
            maanav=pickle.load(f)
            maanav.disp()
            print(maanav.name)
            
    except EOFError:
        print("Done with object")

