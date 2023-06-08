This text file describes the contents of each file required to run the simulation and how to run it.
It is a simulation of an N-Body gravitational system, currently configured to simulate our solar system.
There are 4 files required to run the simulation:

BodyClass.py: 
(No user interaction required)

A class which initialises each body you intend to use in the simulation, asigning it:
name, mass, postion vector, velocity vector, acceleration vector, method and gravitational potential energy. 
It contains two methods by which you can update the position and velocity, the Euler-Cromer algorithm  and the euler forward 
method. There is a setMethod method which is called in the simulation to allow the user to choose which method they would 
like to use. The class does not return any variables, it just updates them over iterations of the time-step deltaT.

SolarSystemClass.py:
(No user interaction required)

Takes a list of the bodies initialised in the BodyClass and calculates their acceleration due to the gravity of the other 
bodies in the simulation at each time-step using the accelerationUpdate method. It also contains a similar method called 
gravPotentialEnergy which calculates the gravitational potential energy of each body due to the other bodys at each 
time-step. It too returns no variables, only updates them. 

Simulation1.1.py:
(First file to be run)

Imports both BodyClass and SolarSystemClass. Contains data on 11 of the major bodies in the solar system; all planets,
the Sun, Earth's moon and Pluto. The simulation will work for an n-body system, to add more bodies, simply write in the
data for their initial conditions, identify them as a Body type object and add the body to the list 'Bodies'. This file is to 
be run in the python terminal. When you do, you will find a user interface which allows the selection of either method, the 
time-step and the number of years to run the simulation. The file is written to run a simulation with all 11 bodies, to remove 
any, remove the corresponding body from the list 'Bodies'. The file runs the simulation over the given number of years and saves
iterations to a data file every 100 iterations. A rudimentary percentage completion loop has been implemented but only works 
properly if the simulation is run in multiples of 5 years (sorry about that!). It does serve to give some indication of the 
progress in running the file however. The user will be prompted to name the data file in the terminal before the simulation runs.
[Sensible input values are 500 < Time-Step < 2000, 0 < Years < 100] (Running 100 years using all 11 bodies and a timestep of 
1000 will take approximately 1 hour.) 

Analysis1.2:
(Second file to be run)

This file contains functions for analysing the data in the data file that has been made previously. It contains functions 
to make lists of and then plot figures of:

The positions of the planets in the X-Y plane 
The angular momentum of the system over time
The percentage change in angular momentum over time
The kinetic energy of the system over time
The potential energy of the system over time 
Toth of the above energies over time on a single plot (so that they might be compared)
The total energy of the system over time
The percentage change in total energy over time

As well as figures, the average value, standard deviation and minimum and maximum values of each quantity will be printed in the 
terminal when its corresponding graph is displayed. 

Analysis1.2 includes functions such as centreOfMassUpdate which calculates the position of the centre of mass of the system at 
each iteration so that the angular momentum calculation is accurate (rather than just taking the origin to be the centre of
mass at all times; this isn't true as all bodies are moving under gravity.)
Before running the file, the user should create an empty folder, in the folder containing the data file, to which the figures
given by the analysis file will be saved. Again, the user should run the file in the terminal. Upon doing this, the user 
will be prompted to write which folder they would like the figures to be saved to (the one they just made) and then to 
write the name of the file they would like to analyise (the exact name given to the file created using Simulation1.1). This file
should not take longer than 10 seconds to run depending on the size of the data file they are using. once the file has run,
the graphs will be shown one at a time. Magnify the position graph to see the individual orbits!




