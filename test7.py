import easygui,os
response=easygui.enterbox("人不能喝什么水？","第七关")
if response=="薪水":
    easygui.msgbox("答对了！",ok_button="点我结束")
    os.system("python ask.py")
elif response and response!="薪水":
    easygui.msgbox("关键时刻掉链子 ？")
else:
    easygui.msgbox("？")
    os.system("python test7.py")
