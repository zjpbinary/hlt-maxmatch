#逆向最大匹配函数maxmatch
#输入为待匹配句子，字典， 最大词的长度
#返回以'\'分割的句子
def maxmatch(s, d, mlen):
    ll = []
    p1 = len(s)
    while p1!=0:
        for k in range(mlen, 0, -1):
            if p1-k<0:
                continue
            elif s[p1-k:p1] in d:
                ll.append(s[p1-k:p1])
                p1 = p1-k
                break
            elif k==1:
                ll.append(s[p1 - k:p1])
                p1 = p1 - k
    ll.reverse()
    return '\\'.join(ll)

#读入字典
with open('data/word.dict', 'r', encoding='UTF-8') as f1:
    di = f1.read().strip().split()

#读入毛文本
with open('data/data.txt', 'r', encoding='UTF-8') as f2:
    ls = [i.strip() for i in f2.readlines()]
#查找最大词长度
maxlen = max([len(i) for i in di])

#lis存放匹配结果
lis = []
for i in ls:
    lis.append(maxmatch(i, di, maxlen))

#将结果写入data.out文件，以回车分割
with open('data/data.out', 'w', encoding='UTF-8') as f3:
    for i in lis:
        f3.write(i)
        f3.write('\n')
