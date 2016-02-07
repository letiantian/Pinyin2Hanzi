#!/bin/bash
python gen_char.py
python gen_phrase.py

cp result/dag_char.json ../../Pinyin2Hanzi/data
cp result/dag_phrase.json ../../Pinyin2Hanzi/data 