#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

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

def build_translator(lines):
    dict = {}

    for line in lines:
        result = int(line[0])
        doid = line[2]
        sy_word = line[3]
        do_word = line[4]

        if result == 0:
            continue

        dict[sy_word] = (doid,do_word)
    return dict



if __name__ == '__main__':
    old_filepath = 'therapy.csv'
    new_filepath = 'therapy_with_doid.csv'
    dict_filepath = 'translater.csv'


    # 筛选出非重复的列
    results = []
    raw_result = read_csv(old_filepath)
    [results.append(i) for i in raw_result if not i in results]

    # 读取对齐结果,构建对应词典
    trans = build_translator(read_csv(dict_filepath))

    # 加doid
    new_results = []
    for line in results:
        sy_word = line[0]
        therapy = line[1]

        if sy_word in trans:
            doid = trans[sy_word][0]
            do_word = trans[sy_word][1]
            new_results.append((doid,do_word,sy_word,therapy))

    # 写回
    write_csv(new_filepath,new_results)







