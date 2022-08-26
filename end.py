import pygame,sys,easygui,platform
from pygame.locals import *
date=["周日","周一","周二","周三","周四","周五","周六"]
w=date[int(sys.argv[1])]
pygame.init()
canvas=pygame.display.set_mode((1000,600))
canvas.fill((255,255,255))
pygame.display.set_caption("游戏结束")
if platform.system()=="Windows":
    font=pygame.font.SysFont("SimHei",100)
    font1=pygame.font.SysFont("SimHei",50)
    bf=pygame.font.SysFont("SimHei",20)
else:
    font=pygame.font.SysFont("Arial Unicode MS",100)
    font1=pygame.font.SysFont("Arial Unicode MS",50)
    bf=pygame.font.SysFont("Arial Unicode MS",20)
title=font.render("游戏结束",True,(0,0,0))
tip=font1.render("对了，你生日是在"+w+"吧？",True,(0,0,0))
b=bf.render("单击退出",True,(0,0,0))
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            easygui.msgbox("再想想？")
        elif event.type==MOUSEBUTTONDOWN:
            xPos,yPos=pygame.mouse.get_pos()
            if 960<=xPos<=1000 and 0<=yPos<=20:
                easygui.msgbox("拜拜")
                pygame.quit()
                exit()
canvas.blit(title,(300,0))
canvas.blit(b,(920,0))
canvas.blit(tip,(212,550))
pygame.display.update()
while True:
    handleEvent()
