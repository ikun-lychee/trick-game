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
text=font.render("帮我关掉",True,(0,0,0))
button=font.render("窗口",True,(0,0,0))
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==MOUSEBUTTONDOWN:
            mouseX,mouseY=pygame.mouse.get_pos()
            if 550<=mouseX<=650 and 275<=mouseY<=325:
                pygame.quit()
                return "QUIT"
canvas.blit(text,(350,275))
canvas.blit(button,(550,275))
pygame.display.update()
while True:
    event=handleEvent()
    if event=="QUIT":
        break
while True:
    turnback=easygui.msgbox("终于关掉了\n最不像答案的答案就是答案","第二关",ok_button="别点我")
    if turnback:
        os.system("python test2.py")
        break
