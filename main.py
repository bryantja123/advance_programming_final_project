'''
Advance Programming project
Group 9
Bryant Burgos 82874
Sebastian Castro 107094
Paola Osorio 96728
'''


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
    
    #Graphical depiction of moving vehicles
    
    def __init__(self, windowName, height, velocity, start):
        self.windowName = windowName
        self.height = height
        self.velocity = velocity
        self.start = start
        
    def spawn(self, windowName):
        self.proj = Projectile(0, self.velocity, self.height)
        self.icon = Circle(Point(self.start , self.height), 0.15)
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

    def moveRight(self):
        center = self.icon.getCenter()
        while (center.getX() < 6):
            update(35)
            self.update(1/500)
            center = self.icon.getCenter()
            print(center.getX())
        self.despawn()
    
##    def moveLeft(self):
##        center = self.icon.getCenter()
##        while (center.getX() > 0):
##            update(35)
##            self.update(1/500)
##            center = self.icon.getCenter()
##            print(center.getX())
##        self.despawn()

    def hasImpacted():
        return self.impact

    def despawn(self):
        self.icon.undraw()

def main():

    win = GraphWin("Frogger", 600, 700, autoflush = False)
    win.setCoords(0, 0, 6, 7)
    win.setBackground("white")

    drawBackground(win)

    carSim = Vehicle(win, 1, 10, 1)
    carSim.spawn(win)
    carSim.moveRight()
    
    carSim2 = Vehicle(win, 1.5, -10, 3)
    carSim2.spawn(win)

    for i in range (400):
        update(35)
        carSim2.update(1/500)


    alert = Text(Point(3, 3.5), "Click anywhere to exit!")
    alert.setSize(20)
    alert.setTextColor("yellow")
    alert.draw(win)
    win.getMouse()
    alert.undraw()
    win.close()

    pass

#*******************************************************************************************

def drawBackground(windowName):

    windowName.setBackground("medium blue")
    
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


    frogLane = Rectangle(Point(0, 7), Point(6, 6))
    frogLane.setOutline("lime green")
    frogLane.setFill("lime green")
    frogLane.draw(windowName)



#*******************************************************************************************

main()

