# Pinyin2Hanzi

拼音转汉字，可以作为拼音输入法的转换引擎，兼容Python 2、Python 3。

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

```python
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

## 2个候选，使用对数打分
result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhii', 'bu', 'zhi', 'dao'), path_num = 2, log = True)
for item in result:
    print(item.score, item.path)
# 发生KeyError，`zhii`不规范
```

#### 基于DAG的转换
原理是词库+动态规划。

```python
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()

## 2个候选
result = dag(dagparams, ('ni', 'bu', 'zhi', 'dao', 'de', 'shi'), path_num=2)
for item in result:
    print(item.score, item.path)
''' 输出
0.08117536840088911 ['你不知道', '的是']
0.04149191639287887 ['你不知道', '的诗']
'''

## 2个候选，使用对数打分
result = dag(dagparams, ('ni', 'bu', 'zhi', 'dao', 'de', 'shi'), path_num=2, log=True)
for item in result:
    print(item.score, item.path)
''' 输出
-2.5111434226494866 ['你不知道', '的是']
-3.1822566564324477 ['你不知道', '的诗']
'''

## 1个候选
print( dag(dagparams, ['ti', 'chu', 'le', 'bu', 'cuo', 'de', 'jie', 'jve', 'fang', 'an'], path_num=1) )
'''输出
[< score=0.0017174549839096384, path=['提出了', '不错', '的', '解决方案'] >]
'''

## 2个候选，使用对数打分
result = dag(dagparams, ('ni', 'bu', 'zhi', 'dao', 'de', 'shii'), path_num=2, log=True)
print(result)
# 输出空列表，因为`shii`不存在
```

#### 自定义params
实现AbstractHmmParams, AbstractDagParams这两个接口即可。具体可以参考源码。

#### 关于拼音
给出的拼音必须是“规范”的。例如

* 略 -> lve
* 据 -> ju

列举所有“规范”的拼音：
```python
from Pinyin2Hanzi import all_pinyin
for py in all_pinyin():
        print(py)
```

将拼音转换为“规范”的拼音：
```python
from Pinyin2Hanzi import simplify_pinyin

print(simplify_pinyin('lue'))
# 输出：'lve'

print(simplify_pinyin('lüè'))
# 输出：'lve'
```

判断是否是“规范”的拼音：
```python
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

## 训练
原始数据和训练代码在`train`目录下。数据来自[jpinyin](https://github.com/stuxuhai/jpinyin)、[pinyin](https://github.com/overtrue/pinyin)、[搜狗语料库-互联网词库](http://www.sogou.com/labs/dl/w.html)等。处理数据时用到了汉字转拼音
工具[ChineseTone](https://github.com/someus/ChineseTone)。

## 原理
[如何实现拼音与汉字的互相转换](http://www.letiantian.me/2016-02-08-pinyin-hanzi/)

## License
MIT



