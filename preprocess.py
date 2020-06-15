#读入data.conll
with open('data/data.conll', 'r', encoding='UTF-8') as f1:
    l = [i.strip().split('\t') for i in f1.readlines()]

#提取单词存放于列表ldict，组成句子存放于列表ls
s = ''
ls = []
ldict = []
for i in l:
    if i==['']:
        ls.append(s)
        s = ''
    else:
        s+=i[1]
        ldict.append(i[1])

#单词去重
ldict = set(ldict)

#写入词典
with open('data/word.dict', 'w', encoding = 'UTF-8') as f2:
    for i in ldict:
        f2.write(i)
        f2.write(' ')

#写入毛文本
with open('data/data.txt', 'w', encoding = 'UTF-8') as f3:
    for i in ls:
        f3.write(i)
        f3.write('\n')
