# def is_narcissistic(number):
#     unit = number % 10
#     decade = int(number/10) % 10
#     hundred = int(number/100)
#     if unit**3 + decade**3 + hundred**3 == number:
#         return True
#     else:
#         return False


# narcissistic_number = []
# for i in range(100, 1000):
#     if is_narcissistic(i):
#         narcissistic_number.append(i)
#     else:
#         pass
# print(narcissistic_number)


# N = 1000001
# pi4th = 0
# for i in range(1, N):
#     item = 1/(2*i-1)*(-1)**(i+1)
#     pi4th += item
# print(pi4th*4)


import math
def isprime(num):
    i = 2
    while(i<num):
        if num%i == 0:
            return False
        i = i + 1 
    return True


def goldbachresolve(num):
    for i in range(2, num):
        if isprime(i) and isprime(num-i):
            print("我们找到了这两个质数")
            print(f"这两个质数是{i}和{num-i}")
            return True
    print("我们找不到这两个质数")
    return False      

# num = 2020
# goldbachresolve(num)

N = 1000  
def test_goldbach():
    for i in range(10, N, 2):
        if goldbachresolve(i):
            pass
        else:
            return("X")
    return("Yes")
print(test_goldbach())



