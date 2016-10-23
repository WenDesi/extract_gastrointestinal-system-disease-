#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import codecs
import chardet

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




if __name__ == '__main__':
    # 读入英文doid name 对应列表
    eng_filepath = 'doid_name_pairs.csv'
    eng_list = read_csv(eng_filepath)
    eng_dict = {}
    for line in eng_list:
        eng_dict[line[1]] = line[0]

    # 读入中英对照表格，并构建中文词典
    zh_filepath = '../ontology/zh_diseaseName.csv'
    zh_list = read_csv(zh_filepath)
    zh_dict = {}
    for line in zh_list:
        id = eng_dict[line[1]]
        zh_ = line[:1] + line[2:]

        for zh in zh_:
            zh_dict[zh] = id

    # 读入对齐实体列表并找到doid
    same_filepath = 'zlz_suibianba.csv'
    same_list = read_csv(same_filepath)
    for i in xrange(len(same_list)):
        id = zh_dict[same_list[i][1]]
        same_list[i][0] = id


    # 结果写入
    write_csv('zlz_same_entity_with_doid.csv',same_list)



