实现一个简单的Qt图形界面

使用pyintaller生成exe：pyinstaller --onefile my_script.py



需要安装配置PyQt5

Designer.app

pycharm添加External Tools

$ProjectFileDir$



把生成的ui文件转化为py文件

方法一：python -m PyQt5.uic.pyuic demo.py -o demo.py

方法二：pyuic5 demo.ui -o demo.py

配置到pycharm

anoaconda python.exe 位置

-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py