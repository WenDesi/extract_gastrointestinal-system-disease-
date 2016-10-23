# -*- coding: utf-8 -*-

import re
import csv
import codecs




file_obj = codecs.open('new 2.txt','r','utf-8')
result = []
while True:
    line = file_obj.readline()
    line=line.strip('\r\n')
    if not line:
        break
    if '翻译为' not in line:
        continue
    result.append(line)
file_obj.close()

def rebuild_disease(line):
    line = line.replace('n.','')
    line = line.replace(' ','')
    line = line.replace(r'"','')
    line = line.replace(r',','|')

    lines = line.split('|')
    lines = set(lines)
    return list(lines)

writer = csv.writer(file('find_name.csv', 'wb'))

a = re.compile(r'(?<=<).*?(?=>)')
for line in result:
    wds = a.findall(line)

    en = wds[0].replace('-',' ')
    zh = rebuild_disease(wds[1])

    new_line = [zh[0],en]
    new_line.extend(zh[1:])

    writer.writerow(new_line)
