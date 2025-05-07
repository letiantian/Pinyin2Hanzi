# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import DefaultDagParams, break_pinyin, simplify_pinyin
from Pinyin2Hanzi import dag
from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi

hmmparams = DefaultHmmParams()
dagparams = DefaultDagParams()

path_num=6

str = ""

def dag_to_option(item):
    return ''.join(item.path)
    
def transform_by_dag(line):
    return map(dag_to_option, dag(dagparams, line, path_num=path_num))


def transform_by_viterbi(line):
    return map(dag_to_option, viterbi(hmm_params=hmmparams, observations=line, path_num=path_num))

while True:
    line = sys.stdin.readline().strip()
    line = break_pinyin(line)
    if line:
        line = tuple(map(simplify_pinyin, line))
        print(line)
        for result in transform_by_viterbi(line):
            print(result)
    else:
        print("Failed to break pinyin from input")

