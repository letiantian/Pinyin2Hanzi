# coding: utf-8

from __future__ import (print_function, unicode_literals)

import sys
import json

sys.path = ['../..'] + sys.path
from Pinyin2Hanzi import util
from ChineseTone import PinyinHelper, PinyinFormat
import jieba

def cut(s):
    return jieba.cut(s, cut_all=False)


def writejson2file(obj, filename):
    with open(filename, 'w') as outfile:
        data = json.dumps(obj, indent=4, sort_keys=True)
        outfile.write(data)

def readdatafromfile(filename):
    with open(filename) as outfile:
        return json.load(outfile)

result = {}
max_num = 0.
min_num = 100000000000000.


for line in open('./word.txt'):
    line = util.as_text(line.strip())
    if '=' not in line:
        continue
    word, num = line.split('=')
    num = float(num)
    pinyin_list = PinyinHelper.convertToPinyinFromSentence(word, segment=cut)
    pinyins = ','.join(pinyin_list)
    pinyins = util.simplify_pinyin(pinyins)
    result.setdefault(pinyins, {})
    result[pinyins].setdefault(word, 0)
    result[pinyins][word] += num
    max_num = max(max_num, result[pinyins][word])
    min_num = min(min_num, result[pinyins][word])

for line in open('./phrase.txt'):
    line = util.as_text(line.strip())
    if '=' not in line:
        continue
    word, _ = line.split('=')
    num = 1.
    pinyin_list = PinyinHelper.convertToPinyinFromSentence(word, segment=cut)
    pinyins = ','.join(pinyin_list)
    pinyins = util.simplify_pinyin(pinyins)
    result.setdefault(pinyins, {})
    result[pinyins].setdefault(word, 0)
    result[pinyins][word] += num
    max_num = max(max_num, result[pinyins][word])
    min_num = min(min_num, result[pinyins][word])

result['max_num'] = max_num
result['min_num'] = min_num

writejson2file(result, './result/dag_phrase.json')

# with open('./result/dag_phrase.txt', 'w') as output:
#     s = ''
#     for pinyin in result:
#         for word in result[pinyin]:
#             num = result[pinyin][word]
#             s = s + pinyin + '=' + word + '=' + str(num) + '\n'
#     output.write(s)