import pygame
import easygui
import os
import random
import platform
from pygame.locals import *
pygame.init()
canvas=pygame.display.set_mode((1000,600))
canvas.fill((255,255,255))
pygame.display.set_caption("第二关")
if platform.system()=="Windows":
    font=pygame.font.SysFont("SimHei",50)
else:
    font=pygame.font.SysFont("Arial Unicode MS",50)
text=font.render("帮我关掉窗口",True,(0,0,0))
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            easygui.msgbox("hhh你傻")
        elif event.type == WINDOWMINIMIZED:
            pygame.quit()
            return "QUIT"
canvas.blit(text,(350,275))
pygame.display.update()
while True:
    event=handleEvent()
    if event=="QUIT":
        break
os.system("python test2.py")
