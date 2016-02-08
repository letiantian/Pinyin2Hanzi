# coding: utf-8
from __future__ import (print_function, unicode_literals, absolute_import)

from .interface import AbstractDagParams
from .priorityset import PrioritySet
from .util import xrange
import math

def dag(dag_params, pinyin_list, path_num=6, log=False):

    assert( isinstance(dag_params, AbstractDagParams) )

    pinyin_num = len(pinyin_list)
    if pinyin_num == 0:
        return []

    D = [PrioritySet(path_num) for _ in xrange(pinyin_num)]

    ## idx is 1
    for from_idx in xrange(0, 1):
        for to_idx in xrange(from_idx, pinyin_num):
            kvs = dag_params.get_phrase(pinyin_list[from_idx:to_idx+1], num=path_num)
            for item in kvs:
                word = [item[0]]
                if log:
                    score = math.log(item[1])
                else:
                    score = item[1]
                D[to_idx].put(score, word)

    for from_idx in xrange(1, pinyin_num):
        prev_paths = D[from_idx-1]
        for to_idx in xrange(from_idx, pinyin_num):
            kvs = dag_params.get_phrase(pinyin_list[from_idx:to_idx+1], num=path_num)
            for prev_item in prev_paths:
                for item in kvs:
                    word = prev_item.path + [ item[0] ]
                    if log:
                        score = prev_item.score + math.log(item[1])
                    else:
                        score = prev_item.score * item[1]
                    D[to_idx].put(score, word)

    result = [ item for item in D[-1] ]

    return sorted(result, key=lambda item: item.score, reverse=True)








