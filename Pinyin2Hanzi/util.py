# coding: utf-8
from __future__ import (print_function, unicode_literals, absolute_import)

import os
import sys

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass


PY2 = sys.version_info[0] == 2
if not PY2:
    # Python 3.x and up
    xrange       = range

    def as_text(v):  ## 生成unicode字符串
        if v is None:
            return None
        elif isinstance(v, bytes):
            return v.decode('utf-8', errors='ignore')
        elif isinstance(v, str):
            return v
        else:
            raise ValueError('Unknown type %r' % type(v))

    def is_text(v):
        return isinstance(v, str)

else:
    # Python 2.x
    xrange       = xrange

    def as_text(v):
        if v is None:
            return None
        elif isinstance(v, unicode):
            return v
        elif isinstance(v, str):
            return v.decode('utf-8', errors='ignore')
        else:
            raise ValueError('Invalid type %r' % type(v))

    def is_text(v):
        return isinstance(v, unicode)


def is_chinese(v):
    if is_text(v):
        if len(v) == 0:
            return False
        return all(u'\u4e00' <= c <= u'\u9fff' or c == u'〇' for c in v)
    else:
        raise ValueError('Invalid type %r' % type(v))

def current_dir():
    return os.path.dirname(os.path.realpath(__file__))


__removetone_dict = {
    'ā': 'a',
    'á': 'a',
    'ǎ': 'a',
    'à': 'a',
    'ē': 'e',
    'é': 'e',
    'ě': 'e',
    'è': 'e',
    'ī': 'i',
    'í': 'i',
    'ǐ': 'i',
    'ì': 'i',
    'ō': 'o',
    'ó': 'o',
    'ǒ': 'o',
    'ò': 'o',
    'ū': 'u',
    'ú': 'u',
    'ǔ': 'u',
    'ù': 'u',
    'ü': 'v',
    'ǖ': 'v',
    'ǘ': 'v',
    'ǚ': 'v',
    'ǜ': 'v',
    'ń': 'n',
    'ň': 'n',
    '': 'm',
}

## 由于从 __future__ 导入了 unicode_literals ， 所以字符串默认是unicode的
# for k in __removetone_dict.keys():
#     v = __removetone_dict[k]
#     __removetone_dict.pop(k, None)
#     __removetone_dict[as_text(k)] = as_text(v)

def remove_tone(one_py):
    """ 删除拼音中的音调
    lǔ -> lu
    """
    one_py = as_text(one_py)
    r = as_text('')
    for c in one_py:
        if c in __removetone_dict:
            r += __removetone_dict[c]
        else:
            r += c
    return r


def normlize_pinyin(one_py):
    """ 规范化
    ue -> ve
    """
    if 'ue' in one_py:
        return one_py.replace('ue', 've')
    if 'ng' == one_py:   # 嗯
        return 'en'
    return one_py

def simplify_pinyin(one_py):
    return normlize_pinyin( remove_tone(one_py.lower()) )

# 拼音
__pinyin = set(['gu','qiao','qian','qve','ge','gang','ga','lian','liao','rou','zong',\
    'tu','seng','yve','ti','te','jve','ta','nong','zhang','fan','ma','gua','die','gui',\
    'guo','gun','sang','diu','zi','ze','za','chen','zu','ba','dian','diao','nei','suo',\
    'sun','zhao','sui','kuo','kun','kui','cao','zuan','kua','den','lei','neng','men',\
    'mei','tiao','geng','chang','cha','che','fen','chi','fei','chu','shui','me','tuan',\
    'mo','mi','mu','dei','cai','zhan','zhai','can','ning','wang','pie','beng','zhuang',\
    'tan','tao','tai','song','ping','hou','cuan','lan','lao','fu','fa','jiong','mai',\
    'xiang','mao','man','a','jiang','zun','bing','su','si','sa','se','ding','xuan',\
    'zei','zen','kong','pang','jie','jia','jin','lo','lai','li','peng','jiu','yi','yo',\
    'ya','cen','dan','dao','ye','dai','zhen','bang','nou','yu','weng','en','ei','kang',\
    'dia','er','ru','keng','re','ren','gou','ri','tian','qi','shua','shun','shuo','qun',\
    'yun','xun','fiao','zan','zao','rang','xi','yong','zai','guan','guai','dong','kuai',\
    'ying','kuan','xu','xia','xie','yin','rong','xin','tou','nian','niao','xiu','fo',\
    'kou','niang','hua','hun','huo','hui','shuan','quan','shuai','chong','bei','ben',\
    'kuang','dang','sai','ang','sao','san','reng','ran','rao','ming','null','lie','lia',\
    'min','pa','lin','mian','mie','liu','zou','miu','nen','kai','kao','kan','ka','ke',\
    'yang','ku','deng','dou','shou','chuang','nang','feng','meng','cheng','di','de','da',\
    'bao','gei','du','gen','qu','shu','sha','she','ban','shi','bai','nun','nuo','sen','lve',\
    'kei','fang','teng','xve','lun','luo','ken','wa','wo','ju','tui','wu','le','ji','huang',\
    'tuo','cou','la','mang','ci','tun','tong','ca','pou','ce','gong','cu','lv','dun','pu',\
    'ting','qie','yao','lu','pi','po','suan','chua','chun','chan','chui','gao','gan','zeng',\
    'gai','xiong','tang','pian','piao','cang','heng','xian','xiao','bian','biao','zhua','duan',\
    'cong','zhui','zhuo','zhun','hong','shuang','juan','zhei','pai','shai','shan','shao','pan',\
    'pao','nin','hang','nie','zhuai','zhuan','yuan','niu','na','miao','guang','ne','hai','han',\
    'hao','wei','wen','ruan','cuo','cun','cui','bin','bie','mou','nve','shen','shei','fou','xing',\
    'qiang','nuan','pen','pei','rui','run','ruo','sheng','dui','bo','bi','bu','chuan','qing',\
    'chuai','duo','o','chou','ou','zui','luan','zuo','jian','jiao','sou','wan','jing','qiong',\
    'wai','long','yan','liang','lou','huan','hen','hei','huai','shang','jun','hu','ling','ha','he',\
    'zhu','ceng','zha','zhe','zhi','qin','pin','ai','chai','qia','chao','ao','an','qiu','ni','zhong',\
    'zang','nai','nan','nao','chuo','tie','you','nu','nv','zheng','leng','zhou','lang','e',])

# 声母
__shengmu = set(['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s',])
# 韵母
__single_yunmu = set(['a', 'o', 'e', 'i', 'u', 'v'])
__complex_yunmu = set(['ai','ei','ui','ao','ou','iu','ie','ve','er','an','en','in','un','ang','eng','ing','ong',])

def is_pinyin(v):
    return v in __pinyin

def all_pinyin():
    for _ in __pinyin:
        yield _

def is_shengmu(v):
    return v in __shengmu

def is_single_yunmu(v):
    return v in __single_yunmu

def is_complex_yunmu(v):
    return v in __complex_yunmu

def is_yunmu(v):
    return is_single_yunmu(v) or is_complex_yunmu(v)

def get_shengmu(one_py):
    if len(one_py) == 0:
        return None
    elif len(one_py) == 1:
        if is_shengmu(one_py):
            return one_py
        else:
            return None
    else:
        if is_shengmu(one_py[:2]):
            return one_py[:2]
        elif is_shengmu(one_py[:1]):
            return one_py[:1]
        else:
            return None