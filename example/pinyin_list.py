# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import all_pinyin
from Pinyin2Hanzi import DefaultDagParams

dagparams = DefaultDagParams()

for py in all_pinyin():
    if len(dagparams.get_phrase([py]) ) == 0:
        print(py)


print( dagparams.get_phrase(['ju']) )
print( dagparams.get_phrase(['jve']) )
