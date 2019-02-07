import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *

class Prince(PhysicObject):
    def __init__(self, imgPath, size):
        super().__init__(Vector2(50,250), None, imgPath, size)
        self.imgsMarche = []
        self.i=0
        for i in range(1,5):
            self.imgsMarche.append("../images/walk"+str(i)+".png")

    def flip(self):
        self.img = pygame.transform.flip(self.img, 0, 1)
        self.imgCopie = pygame.transform.flip(self.imgCopie, 0, 1)

    def nextWalkFrame(self,gauche):
        self.loadImage(self.imgsMarche[int(self.i/2)])
        self.i = (self.i + 1)%8
        if not gauche:
            self.flip()

    def putFlower(self):
        if self.parent != None and not self.parent.withFlower:
            self.parent.addFlower()
            self.parent.flower.angleToParent = 0
            self.parent.flower.rotationAngle = 0
            self.parent.flower.rotateAroundParent(-Vector2(1,0).angle_to(self.position - self.parent.position))
