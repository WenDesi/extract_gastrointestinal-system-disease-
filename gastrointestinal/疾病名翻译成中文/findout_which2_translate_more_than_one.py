# -*- coding: utf-8 -*-

import csv

def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rU'))
    for line in reader:
        results.append(line)
    return results


en_ = '../ontology/diseaseName.txt'
zh_ = '../ontology/zh_diseaseName.csv'

en = read_csv(en_)
zh = read_csv(zh_)

en = map(lambda x:x[0],en)
zh = map(lambda x:x[1],zh)

en_dict = {}

for e in en:
    en_dict[e] = 0

for z in zh:
    print z
    if z in en_dict:
        en_dict[z] += 1
        if en_dict[z] > 1:
            print '%s duplicated !!!!' % z
    else:
        print '%s not in dict , warning!!!!' % z
        break