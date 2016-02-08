# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi

hmmparams = DefaultHmmParams()

result = viterbi(hmm_params=hmmparams, observations=('ni', 'hao', 'a'), path_num = 5, log = True)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('ni', 'hao', 'a'), path_num = 2, log = True)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('chuang', 'qian', 'ming', 'yve', 'guang'), path_num = 5)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('chuang', 'qian', 'ming', 'yve', 'guang'), path_num = 2)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')



result = viterbi(hmm_params=hmmparams, observations=('ni', 'zhi', 'bu', 'zhi', 'dao'), path_num = 5)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('wo', 'men', 'dou', 'shi', 'hao', 'ren'), path_num = 5)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('wo', 'men', 'dou', 'shi', 'hao', 'hai', 'zi'), path_num = 5)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('wo', 'bing', 'bu', 'kuai', 'le'), path_num = 2)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('sheng', 'lve'), path_num = 2)
for item in result:
    print(item.score, '/'.join(item.path))

print(20*'--')

result = viterbi(hmm_params=hmmparams, observations=('ren', 'min', 'wu', 'zhuang'), path_num = 2)
for item in result:
    print(item.score, '/'.join(item.path))