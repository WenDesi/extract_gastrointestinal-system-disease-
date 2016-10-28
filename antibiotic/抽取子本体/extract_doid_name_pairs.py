#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import codecs

full_ontology_filepath = u'ontology/antibiotic.owl'

def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rU'))
    for line in reader:
        results.append(line)
    return results

def read_ontology(filepath):
    file_obj = codecs.open(filepath,'r','utf-8')
    try:
        results = file_obj.read()
    finally:
        file_obj.close()
    return results


def write_csv(filepath,llist):
    writer = csv.writer(file(filepath, 'wb'))
    for line in llist:
        writer.writerow(line)

if __name__ == '__main__':

    ontology = read_ontology(full_ontology_filepath)

    pattern= re.compile(r'(?<=<!-- http://purl.obolibrary.org/obo/DOID_).+?</owl:Class>',re.S)
    blocks = pattern.findall(ontology)

    doid_pattern = re.compile(r'(?<=<oboInOwl:id rdf:datatype="http://www.w3.org/2001/XMLSchema#string">DOID:)\d+')
    name_pattern = re.compile(r'(?<=<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">).+(?=</rdfs:label>)')

    results = []
    for block in blocks:
        name = name_pattern.findall(block)[0]
        doid = doid_pattern.findall(block)[0]

        print '%s doid number is %s' % (name,doid)
        results.append([doid,name])

    write_csv('doid_name_pairs.csv',results)














