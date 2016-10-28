# -*- coding: utf-8 -*-

import re
import csv
import codecs

old_disease = '../ontology/diseaseName.txt'
named_disease = 'zh_named_disease.csv'

def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rb'))
    for line in reader:
        results.append(line)
    return results

old = read_csv(old_disease)
old = map(lambda x: x[0], old)
named = read_csv(named_disease)
named = map(lambda x: x[1], named)

old_set = set(old)
named_set = set(named)

unname_set = old_set - named_set

writer = csv.writer(file('zh_unname_disease.csv', 'wb'))
for line in unname_set:
    writer.writerow([line])