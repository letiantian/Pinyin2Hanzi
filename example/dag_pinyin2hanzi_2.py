# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()


print( dag(dagparams, [u'ti', u'chu', u'le', u'jie', u'jve', u'fang', u'an'], path_num=1) )
print( dag(dagparams, [u'ti', u'chu', u'le'], path_num=1) )


print( dag(dagparams, ['jie', 'jve', 'fang', 'an'], path_num=1) )
print( dag(dagparams, ['jie', 'jve'], path_num=1) )
print( dag(dagparams, ['fang', 'an'], path_num=1) )



