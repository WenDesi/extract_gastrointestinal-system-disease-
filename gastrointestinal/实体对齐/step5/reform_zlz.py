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
    zlz_origin_filepath = 'zlz_xianyangailv.csv'
    fomate_zlz_filepath = 'disease_symptom.csv'

    dict = {}
    lines = read_csv(zlz_origin_filepath)
    lines = map(lambda x:[x[0],x[1]],lines)

    for line in lines:
        key = line[0]
        val = line[1]

        if key not in dict:
            dict[key] = [val]
        else:
            dict[key].append(val)

    new_lines = list(dict)
    result = []
    for line in new_lines:
        print type(line)
        new_line = [line]
        new_line.extend(dict[line])
        result.append(new_line)


    write_csv(fomate_zlz_filepath,result)