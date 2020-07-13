# -*- coding: UTF-8 -*-
import winsound
do = 523
re = 587
mi = 659
fa = 698
quad = 200
half = 400
eigh = 100
#winsound.Beep(do,quad)

string1 = '*'
string2 = string1*2
print(string1)
print(string2)    
print(string1*10 + 'hello' + string2*5)
name = "Lisa"
emotion = "happy"
print("%s is %s" % (name, emotion))
print("{} is {}".format(name, emotion))
print(f"{name} is {emotion}.")

name = 'Lisa Cletamis'
#upper() 
#lower()
upperName, lowerName = name.upper(), name.lower()
print('upperCase: ' + upperName)


print('lowerCase: ' + lowerName)
#title()
titleName = upperName.title()
print('titleCase: ' + titleName)

#dir()
#help()

#lstrip()
#rstrip()
#strip()
#中间的空格要用正则表达式去删
string3 = " \tpython ***\n"
print(string3)
string3 = string3.rstrip()
string3 = string3.strip('*')
string3 = string3.strip()
#string3 = string3.lstrip()
print(string3)