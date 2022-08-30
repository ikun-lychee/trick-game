import pygame
import easygui
import platform
import os
from pygame.locals import *
pygame.init()
canvas=pygame.display.set_mode((1000,600))
canvas.fill((255,255,255))
pygame.display.set_caption("第四关")
if platform.system()=="Windows":
    font=pygame.font.SysFont("SimHei",100)
    font1=pygame.font.SysFont("SimHei",50)
    bf=pygame.font.SysFont("SimHei",20)
else:
    font=pygame.font.SysFont("Arial Unicode MS",100)
    font1=font=pygame.font.SysFont("Arial Unicode MS",50)
    bf=pygame.font.SysFont("Arial Unicode MS",20)
title=font.render("帮我把算式调成成立的",True,(0,0,0))
calculation=font1.render("1+1=1",True,(0,0,0))
blank=pygame.image.load("blank.png")
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            easygui.msgbox("别跑！")
        elif event.type==MOUSEWHEEL:
            canvas.blit(blank,(0,0))
            canvas.blit(title,(0,0))
            calculation=font1.render("1x1=1",True,(0,0,0))
            canvas.blit(calculation,(450,275))
            pygame.display.update()
            easygui.msgbox("惊不惊喜，意不意外？")
            pygame.quit()
            return "QUIT"
canvas.blit(title,(0,0))
canvas.blit(calculation,(450,275))
pygame.display.update()
while True:
    state=handleEvent()
    if state:
        break
os.system("python test4.py")
