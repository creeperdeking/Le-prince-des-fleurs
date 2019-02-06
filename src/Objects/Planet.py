import pygame
from pygame.math import Vector2
from Objects.Volcano import *
from Objects.PhysicObject import *
from Objects.Flower import *

class Planet(PhysicObject):
    def __init__(self, imgPath, size, position, rotationSpeed, radius=-1):
        super().__init__(position, None, imgPath, size)
        if radius > -1:
            self.size = (radius, self.size[1])
            
        self.withFlower=False
        self.rotationSpeed=rotationSpeed
        self.rotationAngle=0
        self.prince=None
        self.gravityForce = 50 * self.size[0]
        self.volcano=Volcano("../images/volcan0.png", position, size, self)
        self.flower=Flower("../images/rose.png",position,size,self)

    def addPrince(self,prince):
        self.prince = prince
        self.prince.setParent(self)
        self.prince.isFlying = False
        self.addFlower()

    def removePrince(self, initialSpeed):
        if self.prince != None:
            self.prince.volcano = None
            self.prince.isFlying = True
            self.prince.position = Vector2(self.prince.imgCenter.center)
            self.prince.speedVector = (self.prince.position - self.position).normalize()*initialSpeed
            # self.prince.initialSpeed=Vector2(distance)
            self.prince.setParent(None)
            self.prince=None

    def addFlower(self):
        self.withFlower=True

    def removeFlower(self):
        self.withFlower=False
        
