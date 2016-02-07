# coding: utf-8

from __future__ import (print_function, unicode_literals)

import os
import sys
import json
from ChineseTone import PinyinHelper
import argparse

sys.path = ['../..'] + sys.path
from Pinyin2Hanzi import util

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass


SENTENCE_FILE     = './result/sentence.txt'
WORD_FILE         = './word.txt'
HANZI2PINYIN_FILE = './hanzipinyin.txt'

BASE_START      = './result/base_start.json'
BASE_EMISSION   = './result/base_emission.json'
BASE_TRANSITION = './result/base_transition.json'

def writejson2file(data, filename):
    with open(filename, 'w') as outfile:
        data = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(data)

def topinyin(s):
    """
    s都是汉字
    """
    s = util.as_text(s)
    py_list = PinyinHelper.convertToPinyinFromSentence(s)
    result = []
    for py in py_list:
        py = util.as_text(py)
        if py == '〇':
            result.append('ling')
        else:
            result.append(util.simplify_pinyin(py))

    if ',' in ''.join(result):
        print(s)
        print(''.join(result))
        sys.exit()
    return result

def extract_chinese_sentences(content):
    content = util.as_text(content)
    content = content.replace(' ', '')
    content = content.replace('\t', '')
    sentences = []
    s = ''
    for c in content:
        if util.is_chinese(c):
            s += c
        else:
            sentences.append(s)
            s = ''
    sentences.append(s)

    return [s.strip() for s in sentences if len(s.strip()) > 1]


def process_hanzipinyin(emission):
    ## ./hanzipinyin.txt
    print('read from hanzipinyin.txt')
    for line in open(HANZI2PINYIN_FILE):
        line = util.as_text(line.strip())
        if '=' not in line:
            continue
        hanzi, pinyins = line.split('=')
        pinyins = pinyins.split(',')
        pinyins = [util.simplify_pinyin(py) for py in pinyins]
        for pinyin in pinyins:
            emission.setdefault(hanzi, {})
            emission[hanzi].setdefault(pinyin, 0)
            emission[hanzi][pinyin] += 1



def read_from_sentence_txt(start, emission, transition):
    ## ./result/sentence.txt
    print('read from sentence.txt')
    for line in open(SENTENCE_FILE):
        line = util.as_text(line.strip())
        if len(line) < 2:
            continue
        if not util.is_chinese(line):
            continue

        ## for start
        start.setdefault(line[0], 0)
        start[line[0]] += 1
        
        ## for emission
        pinyin_list = topinyin(line)
        char_list = [c for c in line]

        for hanzi, pinyin in zip(char_list, pinyin_list):
            emission.setdefault(hanzi, {})
            emission[hanzi].setdefault(pinyin, 0)
            emission[hanzi][pinyin] += 1


        ## for transition
        for f, t in zip(line[:-1], line[1:]):
            transition.setdefault(f, {})
            transition[f].setdefault(t, 0)
            transition[f][t] += 1


def read_from_word_txt(start, emission, transition):
    ## ! 基于word.txt的优化
    print('read from word.txt')
    _base = 1000.
    _min_value = 2.
    for line in open(WORD_FILE):
        line = util.as_text(line.strip())
        if '=' not in line:
            continue
        if len(line) < 3:
            continue
        ls = line.split('=')
        if len(ls) != 2:
            continue
        word, num = ls
        word = word.strip()
        num  = num.strip()
        if len(num) == 0:
            continue
        num = float(num)
        num = max(_min_value, num/_base)
        
        if not util.is_chinese(word):
            continue

        ## for start
        start.setdefault(word[0], 0)
        start[word[0]] += num

        ## for emission
        pinyin_list = topinyin(word)
        char_list = [c for c in word]
        for hanzi, pinyin in zip(char_list, pinyin_list):
            emission.setdefault(hanzi, {})
            emission[hanzi].setdefault(pinyin, 0)
            emission[hanzi][pinyin] += num

        ## for transition
        for f, t in zip(word[:-1], word[1:]):
            transition.setdefault(f, {})
            transition[f].setdefault(t, 0)
            transition[f][t] += num


def gen_base():
    """ 先执行gen_middle()函数 """
    start      = {}     # {'你':2, '号':1}
    emission   = {}     # 应该是 {'泥': {'ni':1.0}, '了':{'liao':0.5, 'le':0.5}}  而不是 {'ni': {'泥': 2, '你':10}, 'hao': {...} } × 
    transition = {}     # {'你': {'好':10, '们':2}, '我': {}}

    process_hanzipinyin(emission)
    
    read_from_sentence_txt(start, emission, transition)
    read_from_word_txt(start, emission, transition)

    ## write to file
    writejson2file(start, BASE_START)
    writejson2file(emission, BASE_EMISSION)
    writejson2file(transition, BASE_TRANSITION)


def main():
    gen_base()


if __name__ == '__main__':
    main()
