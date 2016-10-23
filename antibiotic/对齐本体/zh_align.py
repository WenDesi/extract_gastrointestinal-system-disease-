#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import codecs

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



    results = []

    for words_1 in owl:
        max_ = (0,0,'word1','word2')

        id = words_1[0]
        word1 = words_1[1]
        word1_s = word1.lower()
        print words_1[0]


        for word2 in db:
            word2_s = word2.lower()

            score = calEditDistance(word1_s,word2_s)
            if score > max_[0]:
                max_ = (score,id,word1,word2)

        results.append(max_)

    return results


if __name__ == '__main__':
    db_filepath = 'sy_diseaseName.csv'
    owl_filepath = 'doid_name_pairs.csv'
    results_filepath = 'edit_score_min_results.csv'


    db = read_csv(db_filepath)
    owl = read_csv(owl_filepath)

    db = map(lambda x:x[0],db)

    cal_result = cal(db,owl)
    write_csv(results_filepath,cal_result)




