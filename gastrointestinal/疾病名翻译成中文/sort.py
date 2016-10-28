# -*- coding: utf-8 -*-

import csv
import time
import random

from YMT import YMT

unname_disease = 'zh_unname_disease.csv'
temp_named_disease = 'tmp_named_disease.csv'

def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rU'))
    for line in reader:
        results.append(line)
    return results

if __name__ == '__main__':
    feiwu = read_csv('feiwu.csv')
    feiwu = sorted(feiwu,key=lambda x:x[1])

    feiwuwriter = csv.writer(file('feiwu.csv', 'wb'))

    for f in feiwu:
        feiwuwriter.writerow(f)

