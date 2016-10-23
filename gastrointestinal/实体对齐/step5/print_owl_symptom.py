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
    zlz_origin_filepath = 'symptom.csv'

    dict = {}
    lines = read_csv(zlz_origin_filepath)
    lines = map(lambda x:x[0],lines)

    biaozhun = '''

    <!-- http://purl.obolibrary.org/obo/doid.owl#反酸水 -->

    <owl:Class rdf:about="&obo;doid.owl#%s">
        <rdfs:label rdf:datatype="&xsd;string">%s</rdfs:label>
        <rdfs:subClassOf rdf:resource="&obo;doid.owl#症状"/>
    </owl:Class>'''

    for line in lines:
        print biaozhun % (line,line)
