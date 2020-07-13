# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
def joseph(total_num,pop_num):
    ring_list = [ i+1 for i in range(total_num)]
    bias = 0
    print(ring_list)
    while(len(ring_list)>1):
        pop_time = (len(ring_list)+bias)//pop_num
        residue = (len(ring_list)+bias)%pop_num
        pop_index = [ i*3-bias+2 for i in range(pop_time)]
        pop_index.sort(reverse =True)
        for index in pop_index:
            ring_list.pop(index)
        print(ring_list)
        bias = residue

joseph(34,3)
print("")


# 用del命令实现，其中n,k,s分别表示总人数、kill的编号和最后幸存者的数量。
def joseph_survivor(n,k,s):
    person_list = []
    for i in range(1,n):
        person_list.append(i)
    index,count = 0,1
    list_len = len(person_list)
    while (list_len>s):
        while(index<list_len):
            if count==k:
                del person_list[index]
                count = 0
                index -= 1
            list_len = len(person_list)
            if list_len==s:
                break
            index += 1
            count += 1
        index = 0
    return person_list
print(joseph_survivor(42,3,1))



# for 循环实现
num = 41	#总人数为41人
suv = 2		#幸存者为2人
step = 3 	#数到3处决1人
index = 0	#初始的index编号从0开始
lst = [i+1 for i in range(num)]		#列表生成式生成一个41位长度的数字列表代表打开的环
def update_index(index,lst_length):	#根据index和列表长度的关系更新index值
	if (index + step - 1) >= lst_length-1:	#如果列表太短，那么需要考虑循环计数的情况
		index = (index + step -1 -lst_length)%lst_length
	else:
		index = index + step - 1	#如果列表足够长，那么只需要增加步长-1即可
	return index 					#最后返回更新后的index值，也就是下一个需要处决的人的编号
def kill_popguy(index,lst):
	lst_length = len(lst)
	index = update_index(index,lst_length)		#更新index的值
	popguy = lst.pop(index)						#kill处决对象
	return popguy,index,lst 					#返回处决对象及其编号和更新后的id列表
for i in range(num-suv): 						#逐个kill处决对象，直到剩下2个幸存者
	(popguy,index,lst)=kill_popguy(index,lst)
	# print(popguy,lst)
print(lst) 										#打印幸存者id名单


# 最简代码
num,suv,step,index = 41,2,3,0
lst = [i+1 for i in range(num)]
for i in range(num-suv):
    index = (index + step - 1 - len(lst)) % len(lst)
    lst.pop(index)
print(lst)
