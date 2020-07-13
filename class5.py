#列表分片slice,左闭右开
numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers)

numbers[1:4] = []
print(numbers)
#获取列表长度len()
student_list = ['lilei', 'hanmeimei','madongmei']
print(len(student_list))


#修改列表中的元素
#列表在内存中找了一片相邻的存储空间，索引指向地址
name = ['lilei','hanmeimei']
print(name)

name[0] = 'madongmei'
print(name)

#向列表添加元素
inventory = ['yaoshi','duyao']
print(inventory)
inventory.append('jieyao')
print(inventory)
#删除元素
del inventory[0]
print(inventory)

# 两个列表相加
numbers1 = [0, 1, 2, 3, 4]
numbers2 = [5, 6, 7, 8, 9]
print(numbers1+numbers2)

#判断某个元素是否存在于列表中
if 'jieyao' in inventory:
    print('yes')
else:
    print('no')
#获取列表中某个元素的重复次数
numbers3 = [0,1,1,2,3,4,1]
print(numbers3.count(1))
print(numbers3.count(3))
#获取列表中某个元素第一次出现的位置
print(numbers3.index(4))
#排序
print(sorted(numbers3,reverse = False))#从小到大排序
print(numbers3)
numbers3.sort(reverse = True)#sort()永久排序#从大到小排序
print(numbers3)


string = '132569874'
str_list = list(string)
list_tmp = str_list[::2]#切片 左闭右开，2是步长
list_tmp.sort(reverse=True)
str_list[::2]=list_tmp
print(str_list)


#元组
b = (2,'lilei',19)
#b[0]=1#元组是不可变的
#取值和分片
print(b)
print(b[2])
print(b[0:2])#左闭右开

#for循环
students_list = ["lilei","hanmeimei","madongmei"]
for student in students_list:
    print(student)

for i in range(10):
    print(i)

for i in range(0,10,2):#起始，结束，步长
    print(i)

#if条件判断
score = 86
if score >=90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C" 
else:
    grade = "D"   
print("输入成绩属于级别{}".format(grade))
print(f"输入成绩属于级别{grade}")

available_toppings =["mushrooms","olives","green peppers",
                     "pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print("Adding " + requested_toppings + ".")
    else:
        print("Sorry, we don't have "+requested_toppings + ".")
print("\nFinished make your pizza!")



import math
def isprime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
        return True

for i in range(2,20):
    if isprime(i):
        print(f"{i} is a prime number.")
    else:
        print(f"{i} is not a prime number.")


   
fourth_pi = 0
iter_times = 1000000
for i in range(1, iter_times):
    if i%2 == 1:#不写值的话默认判断是1
        fourth_pi += 1/(2*i-1)
    else:
        fourth_pi -= 1/(2*i-1) 
print(4*fourth_pi)       


print(help(range))