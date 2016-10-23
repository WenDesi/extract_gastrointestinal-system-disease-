#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import codecs
import chardet

from feature import *


def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rU'))
    for line in reader:
        results.append(line)
    return results

def write_csv(filepath,lines):
    writer = csv.writer(file(filepath, 'wb'))
    for line in lines:
        writer.writerow(line)

def cal(db,owl):
    global pinyin

    # 获取拼音
    for words_1 in owl:
        for word1 in words_1:
            get_pinyin(word1)

    for word2 in db:
        get_pinyin(word2)


    results = []
    for word1 in db:
        max_ = (0,'word1','word2')
        print word1
        word1_pinyin = pinyin[word1]

        for words_2 in owl:
            for word2 in words_2:
                word2_pinyin = pinyin[word2]
                score = calEditDistance(word1.decode(),word2.decode())
                # score = calEditDistance(word1_pinyin,word2_pinyin)
                if score > max_[0]:
                    max_ = (score,word2,word1)
        results.append(max_)
    return results

pinyin = {}
p = Pinyin()
def get_pinyin(word):
    global pinyin
    global p
    pinyin[word] = p.get_pinyin(word.decode())

if __name__ == '__main__':
    # 读入张丽珠的先验概率文件，并整合
    zlz_filepath = 'zlz_xianyangailv.csv'
    zlz_disease = list(set(map(lambda x:x[0],read_csv(zlz_filepath))))

    # 读入owl
    owl_filepath = '../ontology/zh_diseaseName.csv'
    owl = map(lambda x:x[:1]+x[2:],read_csv(owl_filepath))
    owl = owl[:-3]

    cal_result = cal(zlz_disease,owl)
    write_csv('zlz_edit_result.csv',cal_result)
