import matplotlib.pyplot as plt 
import math
import numpy as np
import copy

#ADD FITS TO YOUR GRAPH

''' Takes a data file created using Simulation1.1 and performs analysis on it by producing figures, averages and standard deviations. 

Parameters:
DataFile (datafile): a data file made using Simulation1.1 (given via user input of file name upon running the file)
Folder (folder): an empty folder used to store the figures produced (given via user input of folder name upon running the file)
Data Members:
Data (datafile): a data file made using Simulation1.1 (given via user input of file name upon running the file)

Returns:
figurePosition (figure): a figure displaying the positions of each body in the x-y plane (saved into folder)
figureAngularMomentum (figure):a figure displaying the angular momentum of the system over the total run-time (saved into folder), terminal prints the average and standard deviation of the angular momentum
figureKEnergy (figure):a figure displaying the kinetic energy of the system over the total run-time (saved into folder), terminal prints the average and standard deviation of the kinetic energy
figurePEnergy (figure):a figure displaying the potential energy of the system over the total run-time (saved into folder), terminal prints the average and standard deviation of the potential energy
figureKPEnergy (figure):a figure displaying the total energy of the system over the total run-time (saved into folder), terminal prints the average and standard deviation of the total energy

'''

Folder = str(input('What folder would you like to save the figures to?[use exact name of an existing folder]')) # allows users to choose an empty folder to store the figures produced (given via user input of folder name upon running the file)
FileChoice = ('%s.npy'%(str(input('what file would you like to analyse?[use exact name of an existing file without the .npy]')))) # allows users to choose a data file made using Simulation1.1 (given via user input of file name upon running the file)

Data = np.load(FileChoice, allow_pickle=True) # load the data file which the user chooses

BodiesAnalysis = [[] for planets in Data[0][1]] # creates a list of lists of length of no. of bodies data [0]takes the first body (the Sun), [0][1] takes the second iteration of the first body
timeElapsed = [] # a list of times of each iteration
for line in Data:    
    time = line[0]
    timeElapsed.append(time)
    for j in range (len(BodiesAnalysis)): # bodies analysis is now a list which contains the planet number of lists each containing every iteration of said planet 
            body = line[1][j]
            BodiesAnalysis[j].append(body)
        
# Example: print(BodiesAnalysis[0][0].position) # need two indexes as first one tells us its planet 0 (the sun), second one tells us its iteration 0 (at time = 0), .position gives the position array of that planet,at that time


xPos = []# loops to create a list of the lists of y positions of the planets 
for i in range (len(BodiesAnalysis)):# insert a number of empty lists equal to the number of bodies
    xPos.append([])
for z in range(len(BodiesAnalysis)): # z in range number of planets
    for y in range(len(BodiesAnalysis[0])): # y in range number of iterations of each planet (can use zero as iteration number is the same for each planet)
        xPos[z].append(BodiesAnalysis[z][y].position[0]) # fill each empty list with the x positions of the each planet, in order


yPos = [] # loops to create a list of the lists of y positions of the planets 
for i in range (len(BodiesAnalysis)):# insert a number of empty lists equal to the number of bodies
    yPos.append([])
for z in range(len(BodiesAnalysis)): # z in range number of planets 
    for y in range(len(BodiesAnalysis[0])): # y in range number of iterations of each planet (can use zero as iteration number is the same for each planet)
        yPos[z].append(BodiesAnalysis[z][y].position[1]) # fill each empty list with the y positions of the each planet, in order

centreOfMass = [] # a list which will be filled by the function below with the vector position of the centre of mass at each iteration
def centreOfMassUpdate(): # A function which calculates the centre of mass postion vector at each iteration and appends it to a list
    CoM = [[],[],[]] # A list of position vectors of our centre of mass
    for i in range(len(timeElapsed)): # loop over number of iterations, reset each value to zero at the start of the loop 
        totalMass = 0 
        xCoM = 0
        yCoM = 0
        zCoM = 0
        for j in range(len(BodiesAnalysis)): # loop over the total number of planets, calulating centre of mass of each position component for the whole system
            xCoM += BodiesAnalysis[j][i].mass*BodiesAnalysis[j][i].position[0]
            yCoM += BodiesAnalysis[j][i].mass*BodiesAnalysis[j][i].position[1]
            zCoM += BodiesAnalysis[j][i].mass*BodiesAnalysis[j][i].position[2]
            totalMass += BodiesAnalysis[j][0].mass
        CoM[0] = xCoM/totalMass
        CoM[1] = yCoM/totalMass
        CoM[2] = zCoM/totalMass
        centreOfMass.append(CoM) # append each centre of mass vector to the list

angularMomentumList = []  # loops to create a list of the lists of angular momentum magnitudes of the planets
centreOfMassUpdate() # run the function to generate the list of position vectors of centre of mass

for y in range(len(BodiesAnalysis[0])): # y in range number of iterations of each planet (can use zero as iteration number is the same for each planet), resets angular momentum at the start of each loop
    angularMomentum = 0
    for z in range(len(BodiesAnalysis)): # z in range number of planets
        linearMomentum = BodiesAnalysis[z][y].mass*BodiesAnalysis[z][y].velocity
        angularMomentum += (np.cross((BodiesAnalysis[z][y].position-centreOfMass[y]), linearMomentum))
    angularMomentum = np.linalg.norm(angularMomentum) # fill the list with the total angular momentum of the system at each iteration
    angularMomentumList.append(angularMomentum)

changeInAngularMomentum = []
for i in range(len(angularMomentumList)):
    AM_av = np.average(angularMomentumList)
    cAM = ((angularMomentumList[i]-AM_av)/AM_av)*100
    changeInAngularMomentum.append(cAM)



kineticEnergyList = []  # loops to create a list of the lists of kinetic energy of the system over time
for y in range(len(BodiesAnalysis[0])): # y in range number of iterations of each planet (can use zero as iteration number is the same for each planet)
    kineticEnergy = 0
    for z in range(len(BodiesAnalysis)): # z in range number of planets
        
        kineticEnergy += 0.5*(BodiesAnalysis[z][y].mass*np.linalg.norm(BodiesAnalysis[z][y].velocity)*np.linalg.norm(BodiesAnalysis[z][y].velocity)) # fill the list with the total Kinetic Energy of the system at each iteration
    kineticEnergyList.append(kineticEnergy)



potentialEnergyList = []  # loop to create a list of the lists of potential energy of the system over time
for y in range(len(BodiesAnalysis[0])): # y in range number of iterations of each planet (can use zero as iteration number is the same for each planet)
    potentialEnergy = 0
    for z in range(len(BodiesAnalysis)): # z in range number of planets
        
        potentialEnergy += BodiesAnalysis[z][y].potentialEnergy # we define potential energy as negative 
    potentialEnergyList.append(potentialEnergy)


totalEnergyList = [] # loop to create a list of the lists of total energy of the system over time
for y in range(len(BodiesAnalysis[0])): # y in range number of iterations of each planet (can use zero as iteration number is the same for each planet)
    totalEnergy = 0
    totalEnergy += 2*kineticEnergyList[y] + potentialEnergyList[y] # this is the equation for total energy of an N-body system
    totalEnergyList.append(totalEnergy)

changeInTotalEnergy = []
for i in range(len(totalEnergyList)):
    TE_av = np.average(totalEnergyList)
    cTE = ((totalEnergyList[i]-TE_av)/TE_av)*100
    changeInTotalEnergy.append(cTE)



radialdistance = []
def figurePosition(): # Function to plot graph of planet paths
    for l in np.arange(len(BodiesAnalysis)): # a loop to automatically plot the position of each planet in the x-y plane and label it with its name
        plt.plot (xPos[l],yPos[l],'-', label = 'position of %s'%(BodiesAnalysis[l][0].Name))
    plt.xlabel ('x Position [m]')
    plt.ylabel ('y Position [m]')
    plt.legend(loc=1)
    #plt.title ('Positions_%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/Positions_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name 
    plt.show()
for k in np.arange(len(BodiesAnalysis)): # loops to create a list of lists of the positions of the bodes
    radialdistance.append([])
    for l in np.arange(len(BodiesAnalysis[0])):
        x = np.linalg.norm(BodiesAnalysis[k][l].position-BodiesAnalysis[0][l].position)
        radialdistance[k].append(x)

for k in np.arange(len(BodiesAnalysis)): # loops to print the average radial distance of each body from the sun and the standard deviation of this
    print('\nAverage radial distance  of', BodiesAnalysis[k][0].Name,'from the sun =', np.average(radialdistance[k]), 'm' ) # printing the average value and standard devation of the body's position
    print('Standard Deviation in radial distance  of', BodiesAnalysis[k][0].Name,'from the sun =', np.std(radialdistance[k]), 'm\n' )
    print('Minimum radial distance of', BodiesAnalysis[k][0].Name,'from the sun =', np.min(radialdistance[k]), 'm') #printing the min and max value of the body's position
    print('Maximum radial distance of', BodiesAnalysis[k][0].Name,'from the sun =', np.max(radialdistance[k]), 'm')
figurePosition()


def figureAngularMomentum(): # Function to plot graph of angular momentum of system over time
    plt.plot (timeElapsed,angularMomentumList, label = 'Angular Momentum')
    plt.xlabel ('time[s]')
    plt.ylabel ('Angular Momentum [kgm^2/s]')
    plt.legend(loc=2)
    #plt.title ('AngularMomentum_%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/AngularMomentum_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name
    plt.show()
print('\nAverage Angular Momentum of The System =', np.average(angularMomentumList), 'Kgm^(2)s^(-1)' ) # printing the average value and standard devation of the figure
print('Standard Deviation in Angular Momentum of The System =', np.std(angularMomentumList), 'Kgm^(2)s^(-1)\n' )
figureAngularMomentum()

def figurechangeAngularMomentum(): # Function to plot graph of total energy of system over time
    plt.plot (timeElapsed,changeInAngularMomentum, label = 'Change in Angular Momentum')
    plt.xlabel ('time[s]')
    plt.ylabel ('percentage change')
    plt.legend(loc=2)
    #plt.title ('Change in Angular Momentum _%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/Change in Angular Momentum_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name
    plt.show()
figurechangeAngularMomentum()


                                               
def figureKEnergy(): # Function to plot graph of the kinetic and potential energies of system over time
    plt.plot (timeElapsed,kineticEnergyList,label = 'Kinetic Energy')
    plt.xlabel ('time[s]')
    plt.ylabel ('Energy [J]')
    plt.legend(loc=2)
    #plt.title ('KineticEnergy_%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/KineticEnergy_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name
    plt.show()
print('\nAverage Kinetic Energy of The System =', np.average(kineticEnergyList), 'J' ) # printing the average value and standard devation of the figure
print('Standard Deviation in Kinetic Energy of The System =', np.std(kineticEnergyList), 'J\n' )
figureKEnergy() 


def figurePEnergy(): # Function to plot graph of the kinetic and potential energies of system over time
    plt.plot (timeElapsed,potentialEnergyList, label = 'Potential Energy')
    plt.xlabel ('time[s]')
    plt.ylabel ('Energy [J]')
    plt.legend(loc=2)
    #plt.title ('PotentialEnergy_%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/PotentialEnergy_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name
    plt.show()
print('\nAverage Gravitational Potential Energy of The System =', np.average(potentialEnergyList), 'J' ) # printing the average value and standard devation of the figure
print('Standard Deviation in Gravitational Potential Energy of The System =', np.std(potentialEnergyList), 'J\n' )
figurePEnergy()


def figureKPEnergy(): # Function to plot graph of the kinetic and potential energies of system over time
    plt.plot (timeElapsed,kineticEnergyList, label = 'Kinetic Energy')
    plt.plot (timeElapsed,potentialEnergyList, label = 'Potential Energy')
    plt.xlabel ('time[s]')
    plt.ylabel ('Energy [J]')
    plt.legend(loc=2)
    #plt.title ('Kinetic_and_Potential_Energy_%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/Kinetic_and_Potential_Energy_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name
    plt.show()
figureKPEnergy()


def figuretotalEnergy(): # Function to plot graph of total energy of system over time
    plt.plot (timeElapsed,totalEnergyList, label = 'Total Energy')
    plt.xlabel ('time[s]')
    plt.ylabel ('Energy [J]')
    plt.legend(loc=2)
    #plt.title ('TotalEnergy_%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/TotalEnergy_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name
    plt.show()
print('\nAverage Total Energy of The System =', np.average(totalEnergyList), 'J' ) # printing the average value and standard devation of the figure
print('Standard Deviation in Total Energy of The System =', np.std(totalEnergyList), 'J\n' )
figuretotalEnergy()


def figurechangeTotalEnergy(): # Function to plot graph of total energy of system over time
    plt.plot (timeElapsed,changeInTotalEnergy, label = 'Change in Total Energy')
    plt.xlabel ('time[s]')
    plt.ylabel ('percentage change')
    plt.legend(loc=2)
    #plt.title ('Change in Total Energy_%s'%(FileChoice)) # Titles the figure using the file name 
    plt.savefig('%s/Change in Total Energy_%s.png'%(Folder, FileChoice),bbox_inches = 'tight') # saves the figure into the chosen folder and names it using the file name
    plt.show()
figurechangeTotalEnergy()


