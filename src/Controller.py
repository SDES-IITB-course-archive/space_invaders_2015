import pygame
import time
from copy import copy
from sprites import *

class Controller():
    _score = 0;
    def __init__(self,n,m,screen):
        self._font = pygame.font.SysFont("monospace", 16)
        self.scoretext = self._font.render("Score = "+str(self._score), 1, (0,255,0))
        self._screen = screen
        self._rowNo = n;
        self._columnNo = m;
        self.direction ="LEFT"
        self.moveDownFlag = 0
        self.enemyArray = []
        for i in range(self._rowNo):
            self.enemyArray.append([])
            for j in range(self._columnNo):
                enemy1 = Enemy([15,10],[60+i*30,80+j*25],1)
                self.enemyArray[0].append(copy(enemy1))
              #  self.enemyArray[i].append(1)

    def blit(self):
        self.moveDownFlag =  self.moveDownFlag +1
        self.checkDirection()
        self._screen.blit(self.scoretext,(50,50))
        for enemylist in self.enemyArray:
            for enemy in enemylist:
                if (enemy.enemyFlag == 1):
                    enemy.updateDirection(self.direction)
                    self._screen.blit(enemy.image,enemy.rect)
                    enemy.update()
                    if (self.moveDownFlag  == 200):
                        enemy.moveDown();
        if (self.moveDownFlag  == 200):
            self.moveDownFlag = 0

    def checkDirection(self):
        for enemylist in self.enemyArray:
            for enemy in enemylist:
                if (enemy.enemyFlag == 1):
                    if (enemy.checkposX() == 1):
                        self.direction = "LEFT"
                    if (enemy.checkposX() == -1):
                        self.direction = "RIGHT";

    def collision(self,bullet):
        for enemylist in self.enemyArray:
            for enemy in enemylist: 
                self.collision_check(enemy,bullet)

    def collision_check(self,enemy,bullet):
        if (enemy.enemyFlag == 1):
            if bullet.bulletFlag and enemy.rect.colliderect(bullet.rect):
                enemy.enemyFlag = 0
                enemy.rect =None
                bullet.bulletFlag = 0
                self._score = self._score + 100;
                self.scoretext = self._font.render("Score = "+str(self._score), 1, (0,255,0))
                self._screen.blit(self.scoretext,(50,50))