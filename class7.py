# 列表
names = ["lilei","hanmeimei","madongmei"]
phone_numbers = ["1234","3456","0123"]
print(phone_numbers[names.index("lilei")])

phone_numbers = ["lilei","1234","hanmeimei","3456","madongmei","0123"]
print(phone_numbers[phone_numbers.index("lilei")+1])

# 字典
phone_numbers = {"lilei":"1234","hanmeimei":"3456","madongmei":"0123"}
print(phone_numbers["lilei"])

# 用dict函数创建字典
# 根据其他序列新建字典
message = [("lilei",98),("hanmeimei",99)]
d = dict(message)
print(d)
# 根据关键字参数新建字典
d = dict(lilei = 98, hanmeimei = 99)
print(d)

# 访问字典数据
grade = {"lilei":"98","hanmeimei":"99"}
print(grade["lilei"])

# 更新字典元素
grade["hanmeimei"] = 100
print(grade)
# 添加一个key：value对
grade["madongmei"] = "95"
print(grade)

del grade["lilei"]
print(grade)
grade.clear()
print(grade)
del grade# 删除字典本身
# print(grade)

# 字典遍历
favorite_languages = {
    "jen":"python",
    "sarch":"c",
    "edward":"ruby",
    "phil":"python"
}
# #根据key遍历
# for friend in favorite_languages:
# #根据value遍历
# for language in favorite_languages.values():
# #根据items遍历
# for friend, language in favorite_languages.items():
    
    
# 嵌套字典
# 字典列表
student1 = {"name":"JIN","age":"28","grade":"master"}
student2 = {"name":"SUGA","age":"27","grade":"master"}
student3 = {"name":"J-Hope","age":"26","grade":"master"}
student = [student1,student2,student3]
print(student)
# 在字典中存储列表
favorite_class = {
    "JIN":["Vocal"],
    "SUGA":["Rap","PD"],
    "J-Hope":["Dance","Rap","Vocal"],
    }
print(favorite_class["SUGA"])
print(favorite_class["SUGA"][0])
# 在字典中存储字典
class1 = {
    "RM":{"CNAME":"Rap Monster","Rapper":True},
    "Jimin":{"CNAME":"Park Jimin","Rapper":False},
}
print(class1["RM"])
print(class1["Jimin"]["CNAME"])
# 字典的排序

d = {
    "a": 2,
    'b': 5,
    'c': 3
}
# 根据key排序
for k in sorted(d):
    print(k,d[k])
print()
# 根据value排序
for k in sorted(d, key=d.__getitem__,reverse=True):
    print(k,d[k])
print()
# 根据items排序
res = sorted(d.items(),key=lambda d:d[1],reverse=True)
print(res)
# lambda函数是匿名函数，一句话函数，d是形参，d[1]是返回值，用于简单的，不会多次调用的场景


###
##集合
# 创建集合
set1 = {1,2,4,5,8}
set2 = set([1,9,3,2,5])
print(set1)
print(set2)
# 集合的交集intersection
print(set1&set2)
# 集合的并集Union
print(set1|set2)
# 集合的差集Difference 
print(set1-set2)
# 集合的对称差集Symmetric Difference
print(set1^set2)
#set1^set2 = (set1|set2) - (set1&set2)

####
##Input函数的使用
user_gender = input("请输入您的性别（F/M）： ")

if user_gender == "F":
    print("你是女的")
elif user_gender == "M":
    print("你是男的")
else:
    print("你是双性")
    
####
##while循环
i = 1

while i<10:
    print(i)
    i = i + 1

# break和continue
for i in range(10):
    if i ==5:
        break#continue
    print(i)

# while True:
#     pass#占位用的
# #强制退出死循环命令：ctrl C

user_answer_correct = False

while not user_answer_correct:
    user_gender = input("请输入您的性别（F/M）：")
    if user_gender == "F":
        print("你是女的")
        user_answer_correct = True
    elif user_gender == "M":
        print("你是男的")
        user_answer_correct = True
    else:
        print("输入不正确，请重新输入")