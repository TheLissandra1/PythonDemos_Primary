# -*- coding: UTF-8 -*-
#利用pywin32模块，来实现微软的语音接口调用
#安装pip3 install pywin32
import win32com.client
#微软这个服务器
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("hello, how are you?")
import pyttsx3
engine = pyttsx3.init()
#engine.say('君不见，黄河之水天上来，奔流到海不复回。')
#engine.say('君不见，高堂明镜悲白发，朝如青丝暮成雪。')
engine.say('Fine. Bye bitch!')
#运行并且等待
engine.runAndWait()