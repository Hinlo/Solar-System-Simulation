import numpy as np

class Body:
    
    ''' Takes initial position,velocity and acceleration vectors and simulates a body moving under the gravity of other bodies using the Euler algorithms to update the velocity and position.
    
    Parameters:
    Initial position (numpy array): the starting position vector of the body
    Initial velocity (numpy array): the starting velocity vector of the body
    Initial acceleration (numpy array): the starting acceleration vector of the body 
    Name (string): The name of your body
    mass (float): The mass of your body 
    method (int): The number which selects the method you use to update position and velocity
    potentialEnegy (float): the potential energy of the body due to the other bodies
    
    Data Members:
    position (numpy array): the  position vector of the body
    velocity (numpy array): the velocity vector of the body
    acceleration (numpy array): the acceleration vector of the body (updated using SolarSystemClass)
    Name (string): The name of the body
    mass (float): the mass of the body
    method (int): the method you use to update position and velocity
     
    Returns:
    None (the class simply updates the values of the data members)
    '''  

    def __init__ (self, initialPosition, initialVelocity, initialAcceleration, Name, mass, method, potentialEnergy):
        self.position = np.array(initialPosition)
        self.velocity = np.array(initialVelocity)
        self.acceleration = np.array(initialAcceleration)
        self.Name = Name
        self.mass = mass
        self.potentialEnergy = potentialEnergy
        self.setMethod(method)

    def setMethod(self, method): # method to choose the method by which the simulation updates the position and velocity of the bodies
        self.methodchoice = self.eulerCromer
        if method == 2:
            self.methodchoice = self.eulerForward
        

    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def update(self, deltaT):# method make sure the simulation uses the method chosen in setMethod
        self.methodchoice(deltaT)
    
    def eulerCromer(self, deltaT):# method to update position and velocity using the Euler-Cromer algorithm
        self.velocity = self.velocity + (self.acceleration*deltaT)
        self.position = self.position + (self.velocity*deltaT)
        
    def eulerForward(self, deltaT):# method to update position and velocity using the Euler Forward algorithm
        self.position = self.position + (self.velocity*deltaT)     
        self.velocity = self.velocity + (self.acceleration*deltaT)
        


    #Data Members
    position = np.array([0., 0., 0.])
    velocity = np.array([0., 0., 0.])
    acceleration = np.array([0., 0., 0.]) 
    Name = ('Name')
    mass = 1
    potentialEnergy = 0.
    method = eulerCromer