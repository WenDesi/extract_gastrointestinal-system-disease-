#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

from zh_align import *

results = read_csv('align_helper.csv')

for i, line in enumerate(results):
    val = int(line[4])
    if val == 1:
        continue

    print 'row:%d' % (i + 1)

    word1 = line[2]
    word2 = line[3]



    print word1+'\r\n' + word2

    whatever = raw_input()


