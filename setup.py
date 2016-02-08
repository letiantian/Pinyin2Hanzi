# -*- coding: utf-8 -*-
from distutils.core import setup
LONGDOC = """
Engine of Chinese Input Method.

Please go to https://github.com/someus/Pinyin2Hanzi for more info.

具体使用请移步 https://github.com/someus/Pinyin2Hanzi 。
"""

setup(
    name='Pinyin2Hanzi',
    version='0.1.1',
    description='拼音转汉字， Engine of Chinese Input Method',
    long_description=LONGDOC,
    author='Letian Sun',
    author_email='sunlt1699@gmail.com',
    url='https://github.com/someus/Pinyin2Hanzi',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
    ],
    keywords='NLP,Chinese,Pinyin',
    packages=['Pinyin2Hanzi'],
    package_dir={'Pinyin2Hanzi':'Pinyin2Hanzi'},
    package_data={'Pinyin2Hanzi':['*.*','data/*']}
)