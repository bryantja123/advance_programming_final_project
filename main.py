'''
CECS 3210: Advanced Programming Final Project
Group #9
Paola Osorio #96728
Bryant Burgos #82874
Sebastian Castro #107094
'''

#Using the cannonball exercise from the Zelle book as reference
#for making multiple objects move ("animation2.py")

from graphics import *
from projectile import Projectile
from vehicle import Vehicle

class Frog: #<--Placeholder

    def __init__(self, windowName):
        self.windowName = ""

    def drawFrog(self, windowName):
        pass

    def moveUp(self, windowName):
        pass

    def moveDown(self, windowName):
        pass

    def moveLeft(self, windowName):
        pass

    def moveRight(self, windowName):
        pass

#2 rows move to the left; 3 to the right.

class Plow(Vehicle): #Right facing sprite
    
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height, self.start)
        self.icon = Image(Point(self.start , self.height), "plowSprite.gif")
        self.icon.draw(windowName)

class Truck(Vehicle): #Left facing sprite
    
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height, self.start)
        self.icon = Image(Point(self.start , self.height), "truckSprite.gif")
        self.icon.draw(windowName)

class RaceCar(Vehicle): #Right facing sprite
    
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height, self.start)
        self.icon = Image(Point(self.start , self.height), "carSprite3.gif")
        self.icon.draw(windowName)

class Car(Vehicle): #Left facing sprite
    
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height, self.start)
        self.icon = Image(Point(self.start , self.height), "carSprite.gif")
        self.icon.draw(windowName)

class Coupe(Vehicle): #Right facing sprite
    
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height, self.start)
        self.icon = Image(Point(self.start , self.height), "carSprite2.gif")
        self.icon.draw(windowName)
        

def main():

    win = GraphWin("Frogger", 600, 400, autoflush = False)
    win.setCoords(0, 0, 6, 4)
    win.setBackground("white")

    drawBackground(win)

    controlNote = Text(Point(3, 0.2), "Press Q to stop.")
    controlNote.setSize(12)
    controlNote.setTextColor("yellow")
    controlNote.draw(win)
    
    #Animations are currently choppy, could smooth them out later.

    #Need to adjust different vehicle velocities

    #                     0                         1                          2                         3                          4
    vehicles = [Plow(win, 0.8, 12, 0), Truck(win, 1.3, -8, 6), RaceCar(win, 1.8, 20, 0), Car(win, 2.3, -10, 6), Coupe(win, 2.8, 15, 0)]
    vehicles2 = [Plow(win, 0.8, 12, 0), Truck(win, 1.3, -8, 6), RaceCar(win, 1.8, 20, 0), Car(win, 2.3, -10, 6), Coupe(win, 2.8, 15, 0)]
    #Even indexes move right; odd indexes left.

    for j in range(len(vehicles)):
        vehicles[j].spawn(win)
        
    spawnDelay = 0

    forceStop = False

    while(forceStop == False):

        key = win.checkKey() #checkKey() != getKey()
        if key in ["q", "Q"]:
            forceStop = True

        if key in ["w", "W", "Up"]: #Placeholder for frog movement
            pass
        elif key in ["a", "A", "Left"]:
            pass
        elif key in ["s", "S", "Down"]:
            pass
        elif key in ["d", "D", "Right"]:
            pass

        moveVehicles(vehicles, win)

        spawnDelay = spawnDelay + 1

        if spawnDelay == 20:
            for k in range(len(vehicles2)):
                vehicles2[k].spawn(win)

        if spawnDelay >= 20:
            moveVehicles(vehicles2, win)
                
    controlNote.undraw()
    
    alert = Text(Point(3, 2), "Click anywhere to exit!")

    alert.setSize(20)
    alert.setTextColor("yellow")
    alert.draw(win)
    win.getMouse()
    alert.undraw()
    win.close()

#*******************************************************************************************

def moveVehicles(vehicleList, windowName):
    for i in range(len(vehicleList)):
        update(100)
        if(i % 2 == 0): #Even index
            vehicleList[i].updateRight(1/100)
            if(vehicleList[i].getX() > 6):
                vehicleList[i].despawn()
                vehicleList[i].spawn(windowName)
                
        else:
            vehicleList[i].updateLeft(1/100)
            if(vehicleList[i].getX() < 0):
                vehicleList[i].despawn()
                vehicleList[i].spawn(windowName)

def drawBackground(windowName):

    windowName.setBackground("lime green")
    
    road = Rectangle(Point(0, 0.5), Point(6, 3))
    road.setOutline("black")
    road.setFill("black")
    road.draw(windowName)

    medianStrip = Rectangle(Point(0, 0), Point(6, 0.5))
    medianStrip.setOutline("#800080")
    medianStrip.setFill("#800080")
    medianStrip.draw(windowName)

    upperMS = medianStrip.clone()
    upperMS.move(0, 3)
    upperMS.draw(windowName)

#*******************************************************************************************

main()

