#读取人工标注文件
with open('data/data.conll', 'r', encoding='UTF-8') as f1:
    lis = [i.strip().split('\t') for i in f1.readlines()]

l = []
#ls存储人工标注的二维列表
ls = []
for i in lis:
    if i == ['']:
        ls.append(l)
        l = []
    else:
        l.append(i[1])

#读取算法匹配分词的结果
with open('data/data.out', 'r', encoding='UTF-8') as f2:
    #lt存储逆向最大匹配的二维列表
    lt = [i.strip().split('\\') for i in f2.readlines()]

#tagging函数用于标注序列下标，便于统计评估
def tagging(ll):
    l = []
    cur = 1
    for i in ll:
        #记录每个词的第一个字与最后一个字的下标，组成元组
        l.append((cur, cur+len(i)-1))
        cur = cur+len(i)
    return l

#进行序号标注
ls = [tagging(i) for i in ls]
lt = [tagging(i) for i in lt]

#统计正确识别的词数c1，识别出的个体总数c2
#测试集中存在的个体总数c3
c1, c2, c3 = 0, 0, 0
for i in range(len(ls)):
    c2 += len(lt[i])
    c3 += len(ls[i])
    for j in lt[i]:
        if j in ls[i]:
            c1 += 1

#计算精度与召回率
prec = c1/c2
reca = c1/c3
#计算F值
f_score = prec*reca*2/(prec+reca)
print('分词评价')
print('正确识别的词数:', c1)
print('识别的总词数:', c2)
print('人工标注的总词数:', c3)
print('precision:', prec)
print('recall:', reca)
print('f值:', f_score)