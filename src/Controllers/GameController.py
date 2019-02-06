import pygame
from pygame.math import Vector2


from Objects.Planet import *
from Objects.Object import *
from Objects.Volcano import *
from Objects.VueScreen import *
from Objects.Prince import *
from Objects.PhysicObject import *
from Objects.Etoile import *

from Physics.PhysicEngine import *

import time

class GameController:

    def __init__(self):
        self.vueScreen=VueScreen((1680,980))
        self.PhysicEngine = PhysicEngine()
        self.planetes=[]
        self.etoiles=[]
        self.nbFlowers=0
        self.prince=Prince("../images/animIntro/1.png",(100,100))
        self.PhysicEngine.addPhysicObject(self.prince)
        self.createPlanet("../images/Planet0.png",50,50,500,350,-2)
        self.createPlanet("../images/Planet0.png",500,500,1100,350,0.4)
        self.createPlanet("../images/Planet1.png",300,300,375,750,-0.1)
        self.createPlanet("../images/Planet2.png",200,200,200,150,1, 160)
        self.createPlanet("../images/Planet2.png",100,100,1150,800,-0.7, 160)
        self.createEtoile("../images/Etoile.png",600,600,-1)
        self.createEtoile("../images/Etoile.png",750,50,1)
        self.createEtoile("../images/Etoile.png",200,325,-0.5)
        self.createEtoile("../images/Etoile.png",1400,750,0.5)
        self.createEtoile("../images/Etoile.png",1650,300,3)
        self.createEtoile("../images/Etoile.png",750,920,-2)
        self.createEtoile("../images/Etoile.png",100,900,0.2)
        self.addPrinceOnPlanet(self.planetes[1])
        self.play()

    def PrinceFlight(self, prince):
        for planet in self.planetes:
            distance = prince.position.distance_to(Vector2(planet.position.x,planet.position.y))
            acceleration = planet.gravityForce/(distance*distance)
            normaVect = ((planet.position.x,planet.position.y) - prince.position).normalize()
            temps = 1
            prince.speedVector += normaVect * acceleration * temps
        prince.position += prince.speedVector
        prince.position.x = prince.position.x % 1680
        self.prince.rect = self.prince.img.get_rect(center=self.prince.position)
        self.prince.imgCenter = self.prince.img.get_rect(center=self.prince.rect.center)


    def createPlanet(self,imgPath,width,height,centerPositionx,centerPositiony,rotationSpeed, radius = -1):
        planet = Planet(imgPath,(width,height),Vector2(centerPositionx,centerPositiony),rotationSpeed, radius)
        self.planetes.append(planet)
        self.PhysicEngine.addPhysicObject(planet)
        self.PhysicEngine.addPhysicObject(planet.volcano)
        self.PhysicEngine.addPhysicObject(planet.flower)

    def createEtoile(self,imgPath,centerPositionx,centerPositiony,rotationSpeed):
        etoile = Etoile(imgPath,centerPositionx,centerPositiony,rotationSpeed)
        self.etoiles.append(etoile)

    def addPrinceOnPlanet(self,planet):
        planet.addPrince(self.prince)

    def removePrinceFromPlanet(self,planet,initialSpeed):
        planet.removePrince(initialSpeed)

    def display(self):
        self.vueScreen.window.fill((255,255,255))
        for planet in self.planetes:
            self.vueScreen.window.blit(planet.volcano.img, planet.volcano.imgCenter)
            if planet.isFlower :
                self.vueScreen.window.blit(planet.flower.img, planet.flower.imgCenter)
            self.vueScreen.window.blit(planet.img, planet.imgCenter)
        self.vueScreen.window.blit(self.prince.img, self.prince.imgCenter)
        for etoile in self.etoiles:
            self.vueScreen.window.blit(etoile.imgEtoile,etoile.etoileCenter)

    def play(self):
        done=False
        counter,text=10,"10".rjust(3)
        pygame.time.set_timer(pygame.USEREVENT,1000)
        myfont=pygame.font.SysFont("Consolas",30)
        start = time.time()
        while time.time() - start < .5:
            a = pygame.event.get()
        score=0
        down = False
        posMouse = Vector2(0,0)
        while not done:
            for event in pygame.event.get():
                if self.prince.parent != None:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        down = True
                        posMouse = Vector2(pygame.mouse.get_pos())
                    elif event.type==pygame.MOUSEBUTTONUP:
                        down = False
                        pos2 = Vector2(pygame.mouse.get_pos())
                        distance = posMouse.distance_to(pos2)
                        vitesse = distance*0.08
                        print(vitesse)
                        self.removePrinceFromPlanet(self.prince.parent, vitesse)
                if event.type == QUIT:
                    done=True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.prince.rotateAroundParent(6)
                        print("left pressed")
                    elif event.key == pygame.K_RIGHT:
                        print("right pressed")
                        self.prince.rotateAroundParent(-6)

            if time.time()-start>=180:
                done=True
            else:
                text=myfont.render(str(int(180 -(time.time() -start)))+" seconds left !",True, (0, 0, 0), (32, 48))
            score+=self.nbFlowers
            self.update_etoiles()
            self.update_prince(self.prince)
            for planet in self.planetes:
                planet.volcano.chauffe()
            self.PhysicEngine.updatePhysics()
            score+=self.nbFlowers
            self.display()
            self.vueScreen.window.blit(text,(1450,25))
            textScore=myfont.render("Score :"+str(score),True,(0,0,0),(32,48))
            self.vueScreen.window.blit(textScore,(1450,80))
            pygame.display.update()
            self.vueScreen.clock.tick(50)

    def update_etoiles(self):
        for etoile in self.etoiles:
            etoile.rotationAngle += etoile.rotationSpeed
            etoile.imgEtoile = pygame.transform.rotozoom(etoile.imgEtoileCopie,etoile.rotationAngle,1)
            etoile.etoileCenter = etoile.imgEtoile.get_rect(center=etoile.rectEtoile.center)


    def update_prince(self,prince):
        if prince.isFlying:
            print("-----------------------")
            for planet in self.planetes:
                prince.isColliding(planet)
            self.PrinceFlight(self.prince)
            if prince.speedVector.length()!= 0:
                prince.rotationAngle=Vector2(1,0).angle_to(Vector2(prince.speedVector.x,-prince.speedVector.y))
            prince.imgPrince=pygame.transform.rotozoom(prince.imgCopie,prince.rotationAngle,1)
