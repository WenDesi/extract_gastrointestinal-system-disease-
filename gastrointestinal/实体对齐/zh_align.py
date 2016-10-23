#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import codecs
import chardet

from feature import *

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

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

def contain_zh(word):
    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)

    return match

def zh_filter(line):
    id = line[0]

    names = line[1:]

    zh_names = []
    for name in names:
        if contain_zh(name):
            zh_names.append(name)

    return [id,zh_names]


def cal(db,owl):
    global pinyin

    # 获取拼音
    for words_1 in owl:
        for word1 in words_1:
            get_pinyin(word1)

    for line in db:
        words_2 = line[1]
        for word2 in words_2:
            get_pinyin(word2)


    results = []
    for words_1 in owl:
        max_ = (0,0,'word1','word2')
        print words_1[0]

        for word1 in words_1:
            word1_pinyin = pinyin[word1]

            for line in db:
                id = line[0]
                words_2 = line[1]

                for word2 in words_2:
                    word2_pinyin = pinyin[word2]

                    # score = calEditDistance(word1.decode(),word2.decode())
                    score = calEditDistance(word1_pinyin,word2_pinyin)
                    if score > max_[0]:
                        max_ = (score,id,word1,word2)
        results.append(max_)
    return results

pinyin = {}
p = Pinyin()
def get_pinyin(word):
    global pinyin
    global p
    pinyin[word] = p.get_pinyin(word.decode())


if __name__ == '__main__':
    db_filepath = 'neike.csv'
    owl_filepath = '../ontology/zh_diseaseName.csv'
    results_filepath = 'zh_edit_score_min_results.csv'


    db = read_csv(db_filepath)
    owl = read_csv(owl_filepath)

    # 筛选出中文名
    db = map(zh_filter,db)
    db = filter(lambda x:len(x[1])>0,db)

    owl = map(lambda x:x[:1]+x[2:],owl)
    owl = owl[:-3]

    cal_result = cal(db,owl)
    write_csv(results_filepath,cal_result)




