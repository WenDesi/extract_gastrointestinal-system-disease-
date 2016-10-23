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
    unnames = read_csv(unname_disease)
    unnames = map(lambda x:x[0],unnames)
    random.shuffle(unnames)

    named = read_csv(temp_named_disease)
    named = map(lambda x:x[1],named)

    feiwu = read_csv('feiwu.csv')
    feiwu = map(lambda x:x[0],feiwu)

    ymt = YMT()

    writer = csv.writer(file(temp_named_disease, 'ab'))
    feiwuwriter = csv.writer(file('feiwu.csv', 'ab'))
    time.sleep(30)
    count = 0
    for unname in unnames:
        if unname in named or unname in feiwu:
            continue

        count += 1
        print unname
        translate = ymt.get_word_translate(unname)
        time.sleep(5)


        if translate:
            if translate == -1:
                print '您的访问过于频繁'
                break

            # translate = translate.split(',')
            # translate.insert(1,unname)
            # print translate
            # writer.writerow(translate)

            feiwuwriter.writerow([unname,0])
        else:
            feiwuwriter.writerow([unname,1])

    if count == 0:
        print '没有啦！！再试试其他办法吧'
