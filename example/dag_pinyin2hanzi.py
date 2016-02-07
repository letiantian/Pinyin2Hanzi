# coding: utf-8

import sys
sys.path.append('..')

from Pinyin2Hanzi.implement import DefaultDagParams
from Pinyin2Hanzi.dag import dag

dagparams = DefaultDagParams()


result = dag(dagparams, ['wo'])
for item in result:
    print item.score, '/'.join(item.path)

print 20*'*'

result = dag(dagparams, ['ni', 'hao'])
for item in result:
    print item.score, '/'.join(item.path)

print 20*'*'

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'])
for item in result:
    print item.score, '/'.join(item.path)

print 20*'*'

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=2)
for item in result:
    print item.score, '/'.join(item.path)


print 20*'*'

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=6, log=False)
for item in result:
    print item.score, '/'.join(item.path)

print 20*'*'

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=2, log=False)
for item in result:
    print item.score, '/'.join(item.path)

print 20*'*'

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shi'], path_num=1, log=False)
for item in result:
    print item.score, '/'.join(item.path)

print 20*'='

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', 'de', 'shiiiii'], path_num=1, log=False)
print(result)

print 20*'='

result = dag(dagparams, ['ni', 'bu', 'zhi', 'dao', '的', 'shi'], path_num=1, log=False)
print(result)