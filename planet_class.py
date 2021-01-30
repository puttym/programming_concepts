from math import pi, sqrt

mu = 1.32E20 #Standard gravitational parameter of the Sun
G = 6.67E-11 #Gravitational constant

class Planet:
    
    def __init__(self, semi_major_axis, radius, mass):
        self.semi_major_axis = semi_major_axis
        self.radius = radius
        self.mass = mass
        
    def volume(self):
        return (4/3)*pi*self.radius**3
    
    def orbital_period(self): # Check the formula
        return 2*pi*sqrt(self.semi_major_axis**3/mu)
    
    def density(self):
        return self.mass/self.volume()
    
    def orbital_speed(self): # Check
        return sqrt(mu/self.semi_major_axis)
    
    def escape_velocity(self):
        return sqrt(2*G*self.mass/self.radius)
    
    def accn_gravity(self):
        return G*self.mass/self.radius**2
    
    def print_summary(self):
        print('Vol: %f m3' % self.volume())
        print('Den: %f kg/m3' % self.density())
