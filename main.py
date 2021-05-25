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

##    def moveRight(self):
##        center = self.icon.getCenter()
##        while (center.getX() < 6):
##            update(35)
##            self.update(1/500)
##            center = self.icon.getCenter()
##            print(center.getX()) #<-- for tracking X values,
##        self.despawn()           #    purely for test purposes
##    
##    def moveLeft(self):
##        center = self.icon.getCenter()
##        while (center.getX() > 0):
##            update(35)
##            self.update(1/500)
##            center = self.icon.getCenter()
##            print(center.getX())
##        self.despawn()
##
##    def hasImpacted():
##        return self.impact

    def despawn(self):
        self.icon.undraw()



def main():

    win = GraphWin("Frogger", 600, 400, autoflush = False)
    win.setCoords(0, 0, 6, 4)
    win.setBackground("white")

    drawBackground(win)
    
    #Simultaneous movement using lists was successful
    
    #Animations are currently choppy, could smooth them out later.


    carSims = [Vehicle(win, 0.8, 10, 0), Vehicle(win, 1.3, -10, 6), Vehicle(win, 1.8, 10, 0), Vehicle(win, 2.3, -10, 6), Vehicle(win, 2.8, 10, 0)]
    #Even indexes move right; odd indexes left.

    for j in range(len(carSims)):
        carSims[j].spawn(win)
        

    forceStop = False

    while(forceStop == False):

        key = win.checkKey() #checkKey() != getKey()
        if key in ["q", "Q"]:
            forceStop = True

        for i in range(len(carSims)):
            update(50)
            if(i % 2 == 0): #Even index
                carSims[i].updateRight(1/100)
            else:
                carSims[i].updateLeft(1/100)
                

    alert = Text(Point(3, 2), "Click anywhere to exit!")

    alert.setSize(20)
    alert.setTextColor("yellow")
    alert.draw(win)
    win.getMouse()
    alert.undraw()
    win.close()

#*******************************************************************************************

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

