# Minecraft_Scrolling_Avatar_Player
是一个用来展示Minecraft玩家头像以及对应id的python脚本

旨在为服务器宣传视频展示成员名单时所用

实现方法是通过使用角色图片和文件中的 id 对应生成角色，并在屏幕上移动和绘制角色头像，图像的下方显示对应的字符 id。程序会每隔 600 毫秒添加一个角色，当角色的位置超出屏幕高度时，会从角色列表中移除该角色。在程序的主循环中不断更新角色的位置和状态，并在屏幕上绘制所有角色。程序使用了 Pygame 的定时器和事件处理机制。

## 注意事项：
1.本软件由AISophon(QQ:`2498946652`)自主开发

2.如需转载/修改，需要经过作者AISophon(QQ:`2498946652`)知情并同意，违者必究！

3.该软件仅在'Windows 11 家庭中文版 22H2'上测试。

4.如果使用了其它系统/修改过的系统，作者AISophon(QQ:`2498946652`)不能保证能够成功运行。

5.如果使用了其它系统/修改过的系统，对硬件/软件造成损失的，作者AISophon(QQ:`2498946652`)概不负责！

## 使用教程：
1.下载'MSAP.zip'

2.解压缩'MSAP.zip'

3.打开解压缩'MSAP.zip'的'MSAP'文件夹

4.打开'MSAP'文件夹中的'id.txt'TXT 文本文档

5.输入服务器玩家id，以换行隔开，例如：

  `AISophon`

  `Homo`

  注意：不要在开头先换行，中间不要有空行
  
6.保存'id.txt'TXT 文本文档

7.打开'skin'文件夹

8.将对应的玩家头像(png格式)放入其中(例如：'id.txt'TXT 文本文档中有一个玩家名为'AISophon'，那么请在'skin'文件夹中放入一个32*32的png格式图片，并命名为'AISophon.png')
  注意：若该玩家没有皮肤，程序会自动用'default.png'补全，请不要删除'default.png'！

9.回到'MSAP'文件夹

10.运行'Minecraft_Scrolling_Avatar_Player.exe'应用程序

11.会弹出一个窗口，里面的内容就是结果了

## 悄悄话
如果你喜欢的话，请给仓库点一个star~~

如果有更好的思路，欢迎pr或者提出issue
