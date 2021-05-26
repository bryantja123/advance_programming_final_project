'''
CECS 3210: Advanced Programming Final Project
Group #9
Paola Osorio #96728
Bryant Burgos #82874
Sebastian Castro #107094
'''

from textProjectile import Projectile

def main():

    #Projectile(self, angle, velocity, yinit, xinit)
    
    #                     0                         1                          2                         3                          4
    vehicles =[Projectile(0, 12, 0.8, 0), Projectile(0, -8, 1.3, 6), Projectile(0, 20, 1.8, 0), Projectile(0, -10, 2.3, 6), Projectile(0, 15, 2.8, 0)]
    #Even indexes move right; odd indexes left.

    frog = Projectile(0, 0, 0, 3)

    forceStop = False

    while (forceStop == False):
        
        print("\nEnter the next move (W, A, S, D)")
        key = str(input("[Enter Q to quit.]: "))

        if key in ["q", "Q"]:
            forceStop = True
        else:
            print("Vehicle positions:")
            updateVehicles(vehicles)
             
        if key in ["w", "W"]:
            frog.setY(frog.getY() + 0.1)
            
        elif key in ["a", "A"]:
            frog.setX(frog.getX() - 0.1)
            
        elif key in ["s", "S"]:
            frog.setY(frog.getY() + 0.1)
            
        elif key in ["d", "D"]:
            frog.setX(frog.getX() + 0.1)
            
        print("Your current position:")
        print("(", frog.getX(), ",", frog.getY(), ")")

        for i in (range(len(vehicleList))):
            if(vehicleList[i].getX() == frog.getX() and vehicleList[i].getY() == frog.getY()):
                print("*Splat!* \n You lose!")
                forceStop = True

        if frog.getY() > 3:
            print("You made it across! \n You win!")
            forceStop = True
        
#********************************************************************************************

def updateVehicles(vehicleList):
    for i in (range(len(vehicleList))):
        if(i % 2 == 0): #Even index
            vehicleList[i].update(1/100)
            print("[", i + 1, "]: (", vehicleList[i].getX(), ",", vehicleList[i].getY(), ")")
            if(vehicleList[i].getX() > 6):
                vehicleList[i].setX(0)
                
                
        else:
            vehicleList[i].update(1/100)
            print("[", i + 1, "]: (", vehicleList[i].getX(), ",", vehicleList[i].getY(), ")")
            if(vehicleList[i].getX() < 0):
                vehicleList[i].setX(6)

#********************************************************************************************

main()
