import os
#TXT can't you see me? MV
url = 'https://www.bilibili.com/video/av925749211'
#you-get --playlist -o D:/bilibili/TXT https://www.bilibili.com/video/av925749211
#you-get --playlist -o D:/bilibili/TXT https://www.bilibili.com/video/av49043446/
#you-get -i https://www.bilibili.com/video/av49043446
command = 'you-get --playlist -o D:/bilibili/TXT ' + url
os.system(command)