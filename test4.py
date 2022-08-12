from easygui import msgbox,enterbox
import os
msgbox('''请问：
有一辆公交车
限载30人
原来一人都没有
上了3个人
下了1个人
上了28个人
下了4个人
上了2个人
下了18个人
又上了20个人
''')
np=enterbox("请问有多少人？")
if np!="30":
    msgbox("hhh答错了没想到你连算数都不会")
    exit()
msgbox("大对特对！")
msgbox("但我还有个问题")
nc=enterbox('问题包含几个字？（不包含“请问：”)')
if nc!="57":
    msgbox("大错特错……")
    exit()
msgbox("我")
os.system("python test5.py")
