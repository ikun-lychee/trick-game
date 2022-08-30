import easygui
import os
answer=easygui.enterbox("假如你在一片沙漠\n你面前有两杯水\n1：快乐水\n2：毒水\n你选择什么水？（打序号）","第三关")
if answer and (answer!="1" or answer!="2"):
    easygui.msgbox("你砍了棵仙人掌，喝上了里面的水","第三关")
    os.system("python test3.py")
elif answer=="1":
    easygui.msgbox("你得了骨质疏松，走不动了","第三关")
elif answer=="2":
    easygui.msgbox("你没了","第三关")
else:
    easygui.msgbox("你因为不回答问题而出局","第三关")
