# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import DefaultDagParams, break_pinyin
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()

str = ""

def dag_to_option(item):
    return ''.join(item.path)
while True:
    line = sys.stdin.readline().strip()
    line = break_pinyin(line)
    print(line)
    if line:
        print(line)
        for result in map(dag_to_option, dag(dagparams, line, path_num=6)):
          print(result)



