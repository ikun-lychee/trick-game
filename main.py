import pygame
import platform
import easygui
import os
from pygame.locals import *
pygame.init()
canvas=pygame.display.set_mode((1000,600))
canvas.fill((255,255,255))
pygame.display.set_caption("史上最坑爹的游戏")
if platform.system()=="Windows":
    font=pygame.font.SysFont("SimHei",100)
    font1=pygame.font.SysFont("SimHei",50)
    font2=pygame.font.SysFont("SimHei",20)
else:
    font=pygame.font.SysFont("Arial Unicode MS",100)
    font1=pygame.font.SysFont("Arial Unicode MS",50)
    font2=pygame.font.SysFont("Arial Unicode MS",20)
text=font.render("史上最坑人的游戏",True,(0,0,0))
start=font1.render("开始游戏",True,(0,0,0))
noMouseTip=font2.render("没鼠标的先把鼠标买了再说！",True,(0,0,0))
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==MOUSEBUTTONDOWN and event.button==3:
            mouseX,mouseY=pygame.mouse.get_pos()
            if 400<=mouseX<=600 and 400<=mouseY<=450:
                pygame.quit()
                return "EXIT"
        elif event.type==MOUSEBUTTONDOWN and event.button==1:
            easygui.msgbox("这不是开始按钮")
canvas.blit(text,(100,100))
canvas.blit(start,(400,400))
canvas.blit(noMouseTip,(370,580))
pygame.display.update()
while True:
    event=handleEvent()
    if event=="EXIT":
        break
os.system("python test1.py")
