# hlt-maxmatch
## 逆向最大匹配分词

### 一.目录结构 ###
.\data\:  
    data.conll:数据文件  
    data.txt:生成的毛文本文件  
    word.dict:生成的词典文件  
    data.out:生成的分词结果文件  
.\preprocess.py:生成毛文本与词典  
.\max-match.py:利用逆向最大匹配生成分词结果  
.\eva.py:评价分词结果  
.\README.md:使用说明  
### 二.运行 ###
#### 1.环境
python 3.8  
windows  
#### 2.运行方法
python preprocess.py  
python max-match.py  
python eva.py  
#### 3.参考结果
分词评价  
正确识别的词数：20273  
识别的总词数：20404  
人工标注的总词数：20454  
precision：0.9935796902568124  
recall：0. 991150875134448  
f值：0.9923637965637084  
