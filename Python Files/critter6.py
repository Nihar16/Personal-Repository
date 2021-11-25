class Critter(object):
   total = 0

   def status():
      print( "Total critters", Critter.total )
       
   status1 = staticmethod(status)
    
   def __init__(self, name):
      Critter.total += 1
      

crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

Critter.status()
