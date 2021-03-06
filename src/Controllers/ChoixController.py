import pygame,sys
from pygame.locals import *
import math
from Controllers.GameController import GameController
from Controllers.ScoreController import ScoreController
white = (255,255,255)
black = (0,0,0)
skyblue = (135,206,235)


class ChoixController:

    def __init__(self, screen):
        i=0
        self.clock = pygame.time.Clock()
        self.runned = False
        j=0
        white= (255,255,255)
        self.screen = screen
        self.myFont = pygame.font.SysFont('arial',38)
        self.message=self.myFont.render("",True,white)
        self.score=0
        self.titre=pygame.image.load("../images/titre.png").convert_alpha()
        self.fortgroud = pygame.image.load('../images/menu.png').convert_alpha()
        choix  = self.myFont.render("Choisissez votre niveau : ",True,[135,206,235])
        dida1 = self.myFont.render("Didacticiel 1",True,[135,206,235])
        button_rect_dida1=dida1.get_rect(topleft=(50,300))
        dida2= self.myFont.render("Didacticiel 2",True,[135,206,235])
        button_rect_dida2=dida2.get_rect(topleft=(50,400))
        niv1   = self.myFont.render("Niveau 1",True,[135,206,235])
        button_rect_niv1=niv1.get_rect(topleft=(50,500))
        retour   = self.myFont.render("Retour",True,[135,206,235])
        button_rect_retour=retour.get_rect(topleft=(50,600))
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        self.message1=""
        self.message1=self.myFont.render(self.message1,True,white)
        self.message2=""
        self.message2=self.myFont.render(self.message2,True,white)
        self.message3=""
        self.message3=self.myFont.render(self.message3,True,white)
        self.message4=""
        self.message4=self.myFont.render(self.message4,True,white)
        self.message5=""
        self.message5=self.myFont.render(self.message5,True,white)
        self.message6=""
        self.message6=self.myFont.render(self.message6,True,white)
        self.message7=""
        self.message7=self.myFont.render(self.message7,True,white)
        self.message8=""
        self.message8=self.myFont.render(self.message8,True,white)
        self.message9=""
        self.message9=self.myFont.render(self.message9,True,white)
        while True:
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.titre,(0,0))
            screen.blit(self.fortgroud, (400,100 + math.sin(i)*20))
            i+=0.02
            self.screen.blit(self.message1,(480,310))
            self.screen.blit(self.message2,(465,350))
            self.screen.blit(self.message3,(450,390))
            self.screen.blit(self.message4,(435,430))
            self.screen.blit(self.message5,(450,470))
            self.screen.blit(self.message6,(465,510))
            self.screen.blit(self.message7,(480,550))
            self.screen.blit(self.message8,(495,590))
            self.screen.blit(self.message9,(510,630))
            for event in pygame.event.get():
                if event.type==pygame.MOUSEMOTION:
                    pygame.mouse.get_pos()
                    if button_rect_dida1.collidepoint(event.pos):#event to be changed
                        self.message1=("Ce premier didacticiel")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=(" n'a pas de volcans, un")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("nombre faible de planètes")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=(" et pas de planètes à ")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("antigravité. Il permet de")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("s'entraîner aux mécaniques")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=(" de saut, de gravité,")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=(" des fleurs et des")
                        self.message8=self.myFont.render(self.message8,True,white)
                        self.message9=(" étoiles.")
                        self.message9=self.myFont.render(self.message9,True,white)
                    elif button_rect_dida2.collidepoint(event.pos):#event to be changed
                        self.message1=("Ce deuxième didacticiel")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=("a des volcans, un nombre")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("faible de planètes et ")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=("une planète à antigravité.")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("Il permet de s'entraîner")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("aux mécaniques de saut")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=("de gravité, d'antigravité, ")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=("des fleurs, des étoiles")
                        self.message8=self.myFont.render(self.message8,True,white)
                        self.message9=("et des éruptions.")
                        self.message9=self.myFont.render(self.message9,True,white)
                    elif button_rect_niv1.collidepoint(event.pos):#event to be changed
                        self.message1=("Ce premier niveau a")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=("tous les volcans, un ")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("nombre normal de planètes")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=("et une planète à antigravité.")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("Il permet de profiter de")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("toutes les mécaniques ")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=("différentes du jeu et du")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=("système de score")
                        self.message8=self.myFont.render(self.message8,True,white)
                        self.message9=("et des étoiles.")
                        self.message9=self.myFont.render(self.message9,True,white)
                    else:
                        self.message1=("")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=("")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=("")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=("")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=("")
                        self.message8=self.myFont.render(self.message8,True,white)
                        self.message9=("")
                        self.message9=self.myFont.render(self.message9,True,white)
                elif event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_dida1.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run(1)
                    if button_rect_dida2.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run(2)
                    if button_rect_niv1.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run(3)
                        self.score= ScoreController(self.gameController.score,self.screen)
                    if button_rect_retour.collidepoint(event.pos) or self.runned:#event to be changed
                        return

            # position of buttons can be changed
            screen.blit(choix,(50,200))
            screen.blit(dida1,(50,300))
            screen.blit(dida2,(50,400))
            screen.blit(niv1,(50,500))
            screen.blit(retour,(50,600))
            pygame.display.update()
            self.clock.tick(60)


    def run(self,niv):
        self.runned = True
        self.gameController = GameController(self.screen,True,niv)
