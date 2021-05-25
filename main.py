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


class Vehicle:
    
    #Graphical depiction of vehicle movement using red dots
    
    #Direction is determined by whether the
    #given velocity is positive or negative.
    
    def __init__(self, windowName, height, velocity, start):
        self.windowName = windowName
        self.height = height
        self.velocity = velocity
        self.start = start
        
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height, self.start)
        self.icon = Circle(Point(self.start , self.height), 0.05)
        self.icon.setFill("red")
        self.icon.setOutline("red")
        self.icon.draw(windowName)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def update(self, time):
        self.proj.update(time)
        center = self.icon.getCenter()
        dx = self.proj.getX() - center.getX()
        self.icon.move(dx, 0)

    def updateRight(self, time):
        self.proj.update(time)
        center = self.icon.getCenter()
        dx = self.proj.getX() - center.getX()
        if(center.getX() < 6):
            self.icon.move(dx, 0)

    def updateLeft(self, time):
        self.proj.update(time)
        center = self.icon.getCenter()
        dx = self.proj.getX() - center.getX()
        if(center.getX() > 0):
            self.icon.move(dx, 0)

    def despawn(self):
        self.icon.undraw()



def main():

    win = GraphWin("Frogger", 600, 400, autoflush = False)
    win.setCoords(0, 0, 6, 4)
    win.setBackground("white")

    drawBackground(win)

    controlNote = Text(Point(3, 0.2), "Press Q to stop.")
    controlNote.setSize(12)
    controlNote.setTextColor("yellow")
    controlNote.draw(win)
    
    #Simultaneous movement using lists was successful
    
    #Animations are currently choppy, could smooth them out later.

    #                     0                         1                          2                         3                          4
    carSims = [Vehicle(win, 0.8, 10, 0), Vehicle(win, 1.3, -10, 6), Vehicle(win, 1.8, 10, 0), Vehicle(win, 2.3, -10, 6), Vehicle(win, 2.8, 10, 0)]
    carSims2 = [Vehicle(win, 0.8, 10, 0), Vehicle(win, 1.3, -10, 6), Vehicle(win, 1.8, 10, 0), Vehicle(win, 2.3, -10, 6), Vehicle(win, 2.8, 10, 0)]
    #Even indexes move right; odd indexes left.

    for j in range(len(carSims)):
        carSims[j].spawn(win)
        
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

        moveVehicles(carSims, win)

        spawnDelay = spawnDelay + 1

        if spawnDelay == 25:
            for k in range(len(carSims)):
                carSims2[k].spawn(win)

        if spawnDelay >= 25:
            moveVehicles(carSims2, win)
            
        
##        for i in range(len(carSims)):
##            update(50)
##            if(i % 2 == 0): #Even index
##                carSims[i].updateRight(1/100)
##                if(carSims[i].getX() > 6):
##                    carSims[i].despawn()
##                    carSims[i].spawn(win)
##                    
##            else:
##                carSims[i].updateLeft(1/100)
##                if(carSims[i].getX() < 0):
##                    carSims[i].despawn()
##                    carSims[i].spawn(win)
                
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
        update(50)
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

