import easygui
import os
choice=easygui.buttonbox("想要源代码吗？","问答",("想！","不想……"))
if choice=="想！":
    easygui.msgbox("https://github.com/zj-py-123/games/tree/main","问答")
elif choice=="不想……":
    easygui.msgbox("好吧","问答")
os.system("python test6.py")
