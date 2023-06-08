from BodyClass import Body
from SolarSystemClass import solarSystem
import matplotlib.pyplot as plt 
import math
import numpy as np
import copy

''' Imports the Body Class and SolarSystem Class and uses them to, over a given time, update and record the parameters of each body.  

Parameters:
Bodies (list): A list of Bodies (each defined by the variables initialised in BodyClass) generated using BodyClass
deltaT (float): the size of the time-step between each iteration of the bodies (given in seconds via user input - sensible values would be in the range 500 < deltaT < 2000)
deltaThicc (float): defines the frequency with which an iteration of the bodies is saved to the data file, set as saving an iteration every 100 iterations
totalTime (float): the total time for which the simulation is run, (given in years via user input - sensible values would be in the range 0 < totalTime < 100) 
method (int): The number which selects the method you use to update position and velocity (given via user input)
name (str): the name of the file created when the simulation is complete 
Data Members:
body____ (Body): a list of the initial data which define body ____; this file contains the data for the Sun, all the planets, Earth's Moon and Pluto
Data (list): contains the lists of iterations which is saved to a new file
time (int): time that the simulation is run for, starting at 0, updated in steps of deltaT
TimeThicc (int): time that the simulation is run for, starting at 0, updated in steps of deltaThicc

Returns:
Datafile (datafile): saves a data file into the active folder (named by the user upon running the file)
'''


userMethod = int(input('which method would you like? 1 = Euler-Cromer, 2 = Euler-Forward.')) # allows user to input which method they want to use upon running the simulation

if userMethod != 1 and userMethod != 2: # simple value error to ensure a valid method is chosen
    raise ValueError ('You can only use methods 1 or 2.')

# Initial data for the Sun, all planets, Earth's Moon and Pluto
bodySun = Body([0.,0.,0.],[0.,0.,0.],[0.,0.,0.],'Sun',1.988500e30, userMethod, 0) 
bodyMercury = Body([4.374536572064659E+10,2.214107556950127E+10,-2.203895513169586E+09],[-3.149771100964406E+04,4.561242672245834E+04,6.616691312614869E+03],[0.,0.,0.],'Mercury',3.285e23, userMethod, 0)
bodyVenus = Body([2.739272091510331E+10,1.034442466645071E+11,-1.445163416883573E+08],[-3.371756376534645E+04,8.754648734732039E+03,2.078920113150137E+03],[0,0,0],'Venus',4.867e24, userMethod, 0)
bodyMoon = Body([7.786767049205276E+10,1.260106083260409E+11,-3.940317549269646E+07],[-2.640191040389070E+04,1.636825788409336E+04,6.749719675230637],[0,0.,0.],'Moon',7.348e22, userMethod, 0)
bodyEarth = Body([7.753703252241552E+10,1.258205601734234E+11,-5.532147725395858E+06],[-2.583875466354811E+04,1.550600185331871E+04,-7.187500718321971E-1],[0.,0.,0.],'Earth',5.972e24, userMethod, 0)
bodyMars = Body([2.016476752046015E+11,6.225775071988712E+10,-3.643435304089952E+09],[-6.222619994844175E+03,2.522138026247696E+04,6.811811754693391E+02],[0,0,0],'Mars', 6.39e23, userMethod, 0)
bodyJupiter = Body([-3.606662947981693E+11,-7.163382023384180E+11,1.104531201290467E+10],[1.152278912999085E+04,-5.264225801866817E+03,-2.359468722813196E+02],[0.,0.,0.],'Jupiter',1.898e27, userMethod, 0)
bodySaturn = Body([2.629085765504755E+11,-1.482001007805226E+12,1.529624928939217E+10],[8.993281508471346E+03,1.652675885337956E+03,-3.862520489933386E+02],[0,0,0],'Saturn',5.683e26, userMethod, 0)
bodyUranus = Body([2.557458233202205E+12,1.513728431054077E+12,-2.749550735243422E+10],[-3.507315780532064E+03,5.537942825667759E+03,6.613352426198560E+01],[0,0,0],'Uranus',8.681e25, userMethod, 0)
bodyNeptune = Body([4.331166068690323E+12,-1.138104249522513E+12,-7.639035634116089E+10],[1.356588852330393E+03,5.285529678836857E+03,-1.396568226250610E+02],[0,0,0],'Neptune',1.024e26, userMethod, 0)
bodyPluto = Body([1.759994497407093E+12, -4.722102276027367E+12, -3.891104960917234E+09],[5.209069642855447E+03, 7.302242858696433E+02, -1.588169787824503E+03],[0,0,0],'Pluto',1.307e22, userMethod, 0)

def runSimulation(deltaT,deltaThicc,totalTime,Bodies): # A function which runs an N-Body gravitational simulation over a given time (totalTime) by updating the parameters of each body at regular time-steps (deltaT)
    
    time = 0 # time, timeThicc and Data are Data Members
    timeThicc = 0
    Data   = []
    simulation = solarSystem(Bodies) # run the SolarSystem Class using the desired list of bodies
    
    for _ in np.arange (0,totalTime,deltaThicc): # loop over the total time in steps of deltaThicc
        simulation.gravPotentialEnergy() # run the gravitational potential energy method from SolarSystem Class
        item = [timeThicc,copy.deepcopy(Bodies)] 
        Data.append(item) # add item to the data list
        timeThicc += deltaThicc
        
        for _ in np.arange (0,deltaThicc,deltaT): # loop to update acceleration, velocity and position using the smaller, and therefore and more accurate, time-step deltaT
            time += deltaT
            simulation.accelerationUpdate() # run the acceleration update method from SolarSystem Class 
            percent = (time / totalTime)*100 # this line and 'for loop' form a rudimentary percentage complete loop which gives an indication of how far through the simulation you are
            for n in np.arange (1,10):
                if percent == n*10:
                    print ('Simulation is %s %% complete' %(percent))
            for j in np.arange(len(Bodies)): # loop through the bodies in the system 
                Bodies[j].update(deltaT) # run the velocity and position update method from the Body Class 
            
          
    np.save(name,Data) # save our data list to a new file which is named by the user in the terminal upon running the file 
    
 

Bodies = [bodySun, bodyMercury, bodyVenus, bodyMoon, bodyEarth, bodyMars, bodyJupiter, bodySaturn, bodyUranus, bodyNeptune, bodyPluto] #list of bodies which will be included in the simulation



deltaT = float(input('How long would you like your time step to be (seconds).')) # allows user to input what time-step (in seconds) they want to use upon running the simulation
deltaThicc = 100000 # defines the frequency with which an iteration of the bodies is saved to the data file, set as saving an iteration every 100 iterations
totalTime =365*24*3600*float(input('How long would you like the simulation to run for (years)?')) # allows user to input what total simulation time (in years) they want to use upon running the simulation
if totalTime <= 0 or deltaT <= 0:  # simple value error to ensure valid times are chosen
    raise ValueError('No negative times please.')
name = str(input('What would you like to call your file?')) # allows user to input what name they want to give the file created upon running the simulation

runSimulation(deltaT,deltaThicc,totalTime,Bodies) # run the function