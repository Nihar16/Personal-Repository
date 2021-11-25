class Bird:
	wings=2
	n=0
	def __init__(self):
		Bird.n=+1
	@classmethod
	def fly(cls,nob):
		print(nob, "flies with ",cls.wings, "wings")
	@staticmethod
	def noob():
		 print("Total ",Bird.n, " objects created")

Bird.fly("Sparrow")
Sparrow=Bird()
Bird.noob()
print(Bird.n)
