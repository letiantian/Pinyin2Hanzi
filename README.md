# Pinyin2Hanzi

拼音转汉字，可以作为拼音输入法的转换引擎，兼容Python 2、Python 3

## 安装
Python 2：
```
$ python setup.py install --user
```

Python 3：
```
$ python3 setup.py install --user
```

## 使用
下面的示例在Python 3中运行。

#### 基于HMM的转换
原理是viterbi算法。

```
from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi

hmmparams = DefaultHmmParams()

## 2个候选
result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhi', 'bu', 'zhi', 'dao'), path_num = 2)
for item in result:
    print(item.score, item.path)
'''输出
1.3155294593897203e-08 ['你', '知', '不', '知', '道']
3.6677865125992192e-09 ['你', '只', '不', '知', '道']
'''

## 2个候选，使用对数打分
result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhi', 'bu', 'zhi', 'dao'), path_num = 2, log = True)
for item in result:
    print(item.score, item.path)
'''输出
-18.14644152864202 ['你', '知', '不', '知', '道']
-19.423677486918002 ['你', '只', '不', '知', '道']
'''


result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhii', 'bu', 'zhi', 'dao'), path_num = 2, log = True)
for item in result:
    print(item.score, item.path)
```

#### 基于DAG的转换
原理是词库+动态规划。

```
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()

## 2个候选
result = dag(dagparams, ('ni', 'bu', 'zhi', 'dao', 'de', 'shi'), path_num=2)
for item in result:
    print(item.score, item.path)
''' 输出
0.08117536840088911 ['你不知道', '的', '是']
0.04149191639287887 ['你不知道', '的', '诗']
'''

## 2个候选，使用对数打分
result = dag(dagparams, ('ni', 'bu', 'zhi', 'dao', 'de', 'shi'), path_num=2, log=True)
for item in result:
    print(item.score, item.path)
''' 输出
-2.5111434226494866 ['你不知道', '的', '是']
-3.1822566564324477 ['你不知道', '的', '诗']
'''
```

#### 关于拼音
给出的拼音必须是规范的。例如“略”的音必须是`lve`。

将拼音转换为规范的拼音：
```
from Pinyin2Hanzi import simplify_pinyin

print(simplify_pinyin('lue'))
# 输出：'lve'

print(simplify_pinyin('lüè'))
# 输出：'lve'
```

判断是否是规范的拼音：
```
from Pinyin2Hanzi import is_pinyin

print(is_pinyin('lue'))
# 输出：False

print(is_pinyin('lüè'))
# 输出：False

print(is_pinyin('lvee'))
# 输出：False

print(is_pinyin('lve'))
# 输出：True
```

## License
MIT



