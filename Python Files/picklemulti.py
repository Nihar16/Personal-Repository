import pickle
class Human:
    def __init__(self):
        self.name=input("Enter your name : ")
        self.age=input("Enter your age : ")
    def disp(self):
        print("Hello {}, You are {} year old!".format(self.name,self.age))

num=int(input("Enter the number of people to be entered : "))
with open("HumanMulti.dat", "w+b") as f:
    for i in range(num):
        insaan=Human()
        pickle.dump(insaan,f)

with open("HumanMulti.dat", "rb") as f:
    while True:
        try:
                maanav=pickle.load(f)
                maanav.disp()
                                
        except EOFError:
            print("Done with object")
            break
