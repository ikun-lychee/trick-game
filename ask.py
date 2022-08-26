import easygui,datetime,os
y=int(easygui.enterbox("请输入你的出生年份："))
m=int(easygui.enterbox("请输入你的出生月份："))
d=int(easygui.enterbox("请输入你的出生日："))
w=datetime.datetime(y,m,d).strftime('%w')
os.system("python end.py "+w)
