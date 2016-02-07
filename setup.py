# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='Pinyin2Hanzi',
    version='0.1.0',
    author='Letian Sun',
    author_email='sunlt1699@gmail.com',
    install_requires=['numpy >= 1.7.1',],
    packages=['Pinyin2Hanzi'],
    package_dir={'Pinyin2Hanzi':'Pinyin2Hanzi'},
    package_data={'Pinyin2Hanzi':['*.*','data/*']}
)
