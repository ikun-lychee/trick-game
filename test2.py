import easygui
import os
easygui.msgbox("我赌你定被坑惨了","第三关",ok_button="  ")
answer=easygui.enterbox("假如你在一片沙漠\n你面前有两杯水\n1：尿水\n2：毒水\n你选择什么水？（打序号）","第三关")
if answer and (answer!="1" or answer!="2"):
    easygui.msgbox("对呀！不会拿刀砍一个仙人掌然后榨汁喝吗？无毒的","第三关")
    os.system("python test3.py")
elif answer:
    easygui.msgbox("你没了\n《最不像答案的答案就是答案》","第三关")
else:
    easygui.msgbox("你因为不回答问题而出局","第三关")
