from speech import speech
# 替换所有标点为空格
speech = speech.replace(',',' ')
speech = speech.replace('—',' ')
speech = speech.replace('\n',' ')
speech = speech.replace('.',' ')
words_list = speech.split(' ')
rewds_list = []
count_dict = {}
for word in words_list:
    # 只筛选长度大于2的
	if word.isalpha() and len(word)>2:
		rewds_list.append(word.lower())
words_set = set(rewds_list)
for word in words_set:
	count_dict[word] = rewds_list.count(word)
for key in sorted(count_dict,key=count_dict.__getitem__,reverse=True):
	
	print(key,count_dict[key])
