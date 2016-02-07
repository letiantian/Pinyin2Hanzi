# coding: utf-8

'''
从文章中提取句子，放到sentence.txt中
'''

from __future__ import (print_function, unicode_literals)

import os
import sys
import json
import pypinyin
import argparse

sys.path = ['../..'] + sys.path
from Pinyin2Hanzi import util

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

ARTICLE_DIR     = './article'
SENTENCE_FILE   = './result/sentence.txt'

def topinyin(s):
    """
    s都是汉字
    """
    s = util.as_text(s)
    py_list = pypinyin.lazy_pinyin(s)
    result = []
    for py in py_list:
        py = util.as_text(py)
        if py == '〇':
            result.append('ling')
        else:
            result.append(util.simplify_pinyin(py))

    return result

def extract_chinese_sentences(content):
    content = util.as_text(content)
    content = content.replace(' ', '')
    # content = content.replace('\n', '')
    # content = content.replace('\r', '')
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

def gen_sentence():
    all_files = []
    for root, directories, filenames in os.walk(ARTICLE_DIR):
        for filename in filenames: 
            p = os.path.join(ARTICLE_DIR, filename)
            if p.endswith('.txt'):
                all_files.append(p)
    mid_out = open(SENTENCE_FILE, 'w')
    for fp in all_files:
        print('process '+ fp)
        with open(fp) as out:
            content = out.read()
            sentences = extract_chinese_sentences(content)
            mid_out.write('\n'.join(sentences) + '\n')

    mid_out.close()


def main():
    gen_sentence()

if __name__ == '__main__':
    main()