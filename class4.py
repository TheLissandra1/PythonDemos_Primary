# -*- coding: UTF-8 -*-
import math 
import random
def hello(username, grade):
    #code  
    print("hello! " + username + "\n")
    print("Your grade is " + grade + "\n")

hello("Lisa", "104")

# for i in range (1,10):
#     for j in range(i,10):
#         print(i,'*',j,'=',i*j,end=';\t') #用end参数不会自动换行
#     print('')

a = 1
def hello1():
    global a
    print(a)
    a = 2
print(a)#打印1
hello1()#打印1
print(a)#打印2
hello1()#打印2

#解一元二次方程
# from sympy import Symbol, solve, pprint
# x = Symbol('x')#一定要先调用Symbol
# expr = x**2-3*x-5
# solution = solve(expr,x)
# pprint(solution)


#求解二元一次方程组
# from sympy import Symbol, solve, pprint#导入这三个方法
# x = Symbol('x')
# y = Symbol('y')
# expr1 = 2*x +3*y -6
# expr2 = 3*x +2*y -12
# solution1 = solve((expr1, expr2),dict = True)
# pprint(solution1)

#求解微分
from sympy import *
t = Symbol('t')
S = 5*t**2 + 3*t + 8
dSdt = Derivative(S,t).doit()#Derivative(f,x,order = 1) 表示一阶求导
#也可以用diff(S,t)
print(dSdt)#导数表达式
print(dSdt.subs({t:3}))#t=3时的值,用subs方法赋值

#求解积分
# from sympy import Symbol, Integral, pprint
# x = Symbol('x')
# k = Symbol('k')
# f = k*x
# solution2 = Integral(f,x).doit()
# pprint(solution2)
# result = Integral(f,x,(x,0,2)).doit()
# pprint(result)