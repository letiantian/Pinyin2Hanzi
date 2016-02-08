# coding: utf-8

from __future__ import (print_function, unicode_literals)

import sys
import json

sys.path = ['../..'] + sys.path
from Pinyin2Hanzi import util


pinyin2hanzi_file = '../hmm/result/pinyin2hanzi.txt'
base_emission_file = '../hmm/result/base_emission.json'

output_file = './result/dag_char.json'


def writejson2file(obj, filename):
    with open(filename, 'w') as outfile:
        data = json.dumps(obj, indent=4, sort_keys=True)
        outfile.write(data)

def readdatafromfile(filename):
    with open(filename) as outfile:
        return json.load(outfile)


result = {}

data = readdatafromfile(base_emission_file)

max_num = 0.
min_num = 100000000000000.

for hanzi in data:
    for pinyin in data[hanzi]:
        pinyin = util.simplify_pinyin(pinyin)
        num = data[hanzi][pinyin]
        key = pinyin
        result.setdefault(key, {})
        result[key].setdefault(hanzi, 0)
        result[key][hanzi] += num
        max_num = max(max_num, result[key][hanzi])
        min_num = min(min_num, result[key][hanzi])

for line in open(pinyin2hanzi_file):
    line = util.as_text(line.strip())
    if '=' not in line:
        continue
    pinyin, chars = line.split('=')
    if len(pinyin) == 0 or len(chars) == 0:
        continue

    pinyin = util.simplify_pinyin(pinyin)

    for hanzi in chars:
        key = pinyin
        result.setdefault(key, {})
        result[key].setdefault(hanzi, 0)
        result[key][hanzi] += 1.
        max_num = max(max_num, result[key][hanzi])
        min_num = min(min_num, result[key][hanzi])

result['max_num'] = max_num
result['min_num'] = min_num

writejson2file(result, output_file)


# with open(output_file, 'w') as output:
#     s = ''
#     for pinyin in result:
#         for hanzi in result[pinyin]:
#             num = result[pinyin][hanzi]
#             s = s + pinyin + '=' + hanzi + '=' + str(num) + '\n'
#     output.write(s)