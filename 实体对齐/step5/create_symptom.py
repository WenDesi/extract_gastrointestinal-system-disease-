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

    disease = '12236'

    dict = {}
    lines = read_csv(zlz_origin_filepath)

    biaozhun = '''        <owl:equivalentClass>
            <owl:Restriction>
                <owl:onProperty rdf:resource="&obo;doid#has_symptom"/>
                <owl:someValuesFrom rdf:resource="&obo;doid.owl#%s"/>
            </owl:Restriction>
        </owl:equivalentClass>'''

    for line in lines:
        if line[0] == disease:
            for zz in line[2:]:
                print biaozhun % zz
