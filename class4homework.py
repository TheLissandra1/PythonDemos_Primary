# -*- coding: UTF-8 -*-
def Fahrenheit2Celsius(f):
    #c = 0
    c = 5/9*(f-32)
    print(c)
Fahrenheit2Celsius(104)

def ChickenAndRabbit(n,m):
    c = 2*n -1/2*m
    r = m*1/2 - c*1/2 
    return c,r   

chicken1 = int(ChickenAndRabbit(35,94)[0])
rabbits1 = int(ChickenAndRabbit(35,94)[1])
print(f"There are {chicken1} chicken \n")
print("Chicken: ", chicken1, "\t")
print("rabbit: " , rabbits1)

from sympy import *
x = Symbol('x')
y = Symbol('y')
n = Symbol('n')
m = Symbol('m')
expr1 = x+y-n
expr2 = 2*x+4*y-m
solution = solve((expr1,expr2), (x,y),dict = True)
chicken = solution[0][x].subs({n:35,m:94})
rabbits = solution[0][y].subs({n:35,m:94})
print(f'There are {chicken} chicken')
print(f'There are {rabbits} rabbits')

#循环计算圆周率
fourth_pi = 0
iter_times = 1000000
for i in range(1,iter_times):
    if i%2:
        fourth_pi += 1/(2*i-1)
    else:
        fourth_pi -= 1/(2*i-1)
print(4*fourth_pi)

x = Symbol('x')
f = 1/(1+x**2)
solution0 = Derivative(f,x,order=3).doit()
print(solution0)
result = solution0.subs({x:0})
print(result)


x = Symbol('x')
f = (3*x+6)/((x-1)**2)/(x**2+x+1)
solution1 = Integral(f,x).doit()
pprint(solution1)