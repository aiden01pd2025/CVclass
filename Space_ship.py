import numpy as np
c = 300000000

class spaceship:
	def __init__(self,mass):
		self.mass=mass
	def rel_mass(self,v):
		m0=v**2/c**2
		m0=1-m0
		m0=np.sqrt(m0)
		return(self.mass/m0)

Apollo13 = spaceship(100)
Frankship=spaceship(2000)
print(Apollo13.rel_mass(0.99*c))
print(Frankship.rel_mass(0.99*c))