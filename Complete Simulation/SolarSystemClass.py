import numpy as np
from BodyClass import Body
import math
class solarSystem:
    ''' Takes N bodies defined using the Body Class and calculates their acceleration and potential energies over time. 
    
    Parameters:
    Bodies (list): A list of Bodies (each defined by the variables initialised in BodyClass) generated using BodyClass

    Data Members:
    ListofBodies (list): A list of Bodies (each defined by the variables initialised in BodyClass) generated using BodyClass
    
    Returns:
    None (the class simply updates the values of the acceleration vectors and potential energies)
    '''

    G = -6.674e-11
    ListofBodies =[]
    def __init__(self, Bodies):
        self.ListofBodies = Bodies
        
    def __repr__(self):
        for i in range (len(self.ListofBodies)):
            B = self.ListofBodies[i]
            return ('Body: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(B.Name, B.mass, B.position, B.velocity, B.acceleration))


    
    def accelerationUpdate(self): # a method to use update the acceleration of each of the bodies, due to the gravitational force from all the other bodies, at each iteration of the system 
        
        for i in range(len(self.ListofBodies)): # loops to iterate the acceleration over all bodies in the system 
            self.ListofBodies[i].acceleration = [0,0,0] # reset the acceleration to zero at the start of the outer loop
            for j in range(len(self.ListofBodies)): # loops to iterate the acceleration over all bodies in the system 
                if i!=j:
                    
                    r = self.ListofBodies[i].position-self.ListofBodies[j].position # vector r (the vector separation of the two bodies i and j)
            
                    scalar_r = np.linalg.norm(r)       # numpy function for the modulus, takes argument of r to give |r| 
            
                    unit_r = r/scalar_r #unit vector of r
            
                    self.ListofBodies[i].acceleration += ((self.G*self.ListofBodies[j].mass*unit_r)/(scalar_r * scalar_r)) # equation for acceleration of body i due to body j, the total acceleration of body i is the sum of the acceleration due to all j bodies.


    def gravPotentialEnergy(self):  # a method to use update the gravitational potential energy (GPE) of each of the bodies uses exactly the same logic as the above method except the equation now calculates the gravitational potential energy
        
        for i in range(len(self.ListofBodies)):
            self.ListofBodies[i].potentialEnergy = 0.
            for j in range(len(self.ListofBodies)):
                if i!=j:
                    
                    r = self.ListofBodies[i].position-self.ListofBodies[j].position # vector r (the vector separation of the two bodies i and j)
            
                    scalar_r = np.linalg.norm(r)       # numpy function for the modulus, takes argument of r to give mod(r) 
            
                    self.ListofBodies[i].potentialEnergy += ((self.G*self.ListofBodies[j].mass*self.ListofBodies[i].mass)/(scalar_r)) # equation for GPE of body i due to body j, the total GPE of body i is the sum of the acceleration due to all j bodies.

        
        
        
        
        
