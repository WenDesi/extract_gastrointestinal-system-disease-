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
    result1 = 'edit_dist_result.csv'
    result2 = 'pinyin_edit_dist_result.csv'

    result1 = read_csv(result1)
    result2 = read_csv(result2)

    same = []

    for w1 in result1:
        for w2 in result2:
            if w1[1] == w2[1] and w1[2] == w2[2] and w1[3] == w2[3]:
                same.append(w1)

    write_csv('same_entity.csv',same)



