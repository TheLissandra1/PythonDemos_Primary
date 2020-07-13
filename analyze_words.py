from alice import alice_full_text as aft
punc_lst = ["'",'.',',','?','-','!','\"',':',';','(',')',']','[','_']
for punc in punc_lst:
	aft = aft.replace(punc,' ')
# 用split方法分隔开单词，分离空格之间的
words_list = aft.split()
words_dict = {}
# 创建不重复元素列表words_set
words_set = set(words_list)
words = [] 
# 用count（）方法，统计每个单词的出现次数
for word in words_set:
	words_dict[word] = words_list.count(word)
# 统计words_set列表里有多少元素
print(len(words_set))
stop_words = ['little','again','herself','could','would','There',
				'thought','The','And','You','What','She','But','March']
for word in sorted(words_dict,key = words_dict.__getitem__,reverse = True):
	if len(words)>10:
		break
	if (len(word) > 2) and (word not in stop_words) and (word[0].istitle()==True):
		# print(f'{word}:{words_dict[word]}')
		words.append((word,words_dict[word]))


from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100])
        .set_global_opts(
        	title_opts=opts.TitleOpts(
        		title="CHARACTERS IN ALICE'S ADVENTURES IN WONDERLAND"))
    )
    return c

wd = wordcloud_base()
wd.render()