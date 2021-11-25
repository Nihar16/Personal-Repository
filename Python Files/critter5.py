class Critter(object):
   total = 0

   def __init__(self, name):
      Critter.total += 1
      

crit1=Critter("python")
print( Critter.total )   #the class
print( crit1.total  )    #the instance
#crit1.total += 1  # won’t work;
