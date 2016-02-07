# coding: utf-8

from __future__ import (print_function, unicode_literals)

import sys
import json

sys.path = ['../..'] + sys.path
from Pinyin2Hanzi import util


def writejson2file(obj, filename):
    with open(filename, 'w') as outfile:
        data = json.dumps(obj, indent=4, sort_keys=True)
        outfile.write(data)

def readdatafromfile(filename):
    with open(filename) as outfile:
        return json.load(outfile)

def _filter(s):
    s = s.replace(chr(0), '')
    return s

def get_weight(raw_value, raw_min, raw_max, weight_min, weigth_max):
    raw_value = float(raw_value)
    raw_min = float(raw_min)
    raw_max = float(raw_max)
    weight_min = float(weight_min)
    weigth_max = float(weigth_max)

    weight_diff = weigth_max - weight_min
    bili = (raw_value - raw_min) / (raw_max - raw_min)
    return weight_min + bili * (weigth_max - weight_min)

# print( get_weight(23, 1, 23, 1,  230) )
# 

# 单字权重由0.1到0.2

def gen_dag_char():
    data = readdatafromfile('./result/dag_char.json')
    result = {}
    max_num = data['max_num']
    min_num = data['min_num']
    for pinyin in data:
        if pinyin == 'max_num' or pinyin == 'min_num':
            continue
        for hanzi in data[pinyin]:
            hanzi = _filter(hanzi)
            pinyin = _filter(pinyin)
            num = data[pinyin][hanzi]
            result.setdefault(pinyin, [])
            weight = get_weight(num, min_num, max_num, 0.1, 0.2)
            result[pinyin].append((hanzi, weight))
        result[pinyin] = sorted(result[pinyin], key = lambda item: item[1], reverse=True)

    writejson2file(result, '../../Pinyin2Hanzi/data/dag_char.json')



# 词权重由0.2到1.0

def gen_dag_phrase():
    data = readdatafromfile('./result/dag_phrase.json')
    result = {}
    max_num = data['max_num']
    min_num = data['min_num']
    for pinyin in data:
        if pinyin == 'max_num' or pinyin == 'min_num':
            continue
        for phrase in data[pinyin]:
            phrase = _filter(phrase)
            pinyin = _filter(pinyin)
            num = data[pinyin][phrase]
            result.setdefault(pinyin, [])
            weight = get_weight(num, min_num, max_num, 0.2, 1.0)
            result[pinyin].append( (phrase, weight) )
        result[pinyin] = sorted(result[pinyin], key = lambda item: item[1], reverse=True)

    writejson2file(result, '../../Pinyin2Hanzi/data/dag_phrase.json')


##

gen_dag_char()
gen_dag_phrase()