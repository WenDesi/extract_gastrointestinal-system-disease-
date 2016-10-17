#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import codecs

def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rU'))
    for line in reader:
        results.append(line)
    return results


def write_csv(filepath,llist):
    writer = csv.writer(file(filepath, 'wb'))
    for line in llist:
        writer.writerow(line)

if __name__ == '__main__':
    zlz_origin_filepath = 'zlz_align.csv'
    fomate_zlz_filepath = 'symptom.csv'

    dict = {}
    lines = read_csv(zlz_origin_filepath)
    lines = map(lambda x:x[2:],lines)

    for line in lines:
        for symptom in line:
            dict[symptom] = 1

    new_lines = list(dict)
    result = []
    for line in new_lines:
        result.append([line])


    write_csv(fomate_zlz_filepath,result)