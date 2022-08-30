import pygame
import easygui
import os
import platform
from pygame.locals import *
easygui.msgbox("请记住！\n210103831","第六关","我记住了")
pygame.init()
canvas=pygame.display.set_mode((1000,600))
canvas.fill((255,255,255))
pygame.display.set_caption("第六关")
if platform.system()=="Windows":
    font=pygame.font.SysFont("SimHei",100)
    font1=pygame.font.SysFont("SimHei",50)
    bf=pygame.font.SysFont("SimHei",20)
else:
    font=pygame.font.SysFont("Arial Unicode MS",100)
    font1=font=pygame.font.SysFont("Arial Unicode MS",50)
    bf=pygame.font.SysFont("Arial Unicode MS",20)
text1=font.render("请问你记",True,(0,0,0))
TrueButton=font.render("住",True,(0,0,0))
text2=font.render("了什么？",True,(0,0,0))
falsebutton1=font1.render("A,102840284",True,(0,0,0))
falsebutton2=font1.render("B,103829383",True,(0,0,0))
falsebutton3=font1.render("C,247383721",True,(0,0,0))
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            easygui.msgbox("别跑！")
        if event.type==MOUSEBUTTONDOWN:
            xPos,yPos=pygame.mouse.get_pos()
            if 475<=xPos<=575 and 0<=yPos<=100:
                easygui.msgbox("就是记 住 嘛！","第六关")
                pygame.quit()
                return 1
canvas.blit(text1,(75,0))
canvas.blit(TrueButton,(475,0))
canvas.blit(text2,(575,0))
canvas.blit(falsebutton1,(275,200))
canvas.blit(falsebutton2,(275,250))
canvas.blit(falsebutton3,(275,300))
pygame.display.update()
while True:
    response=handleEvent()
    if response:
        break
os.system("python test7.py")
