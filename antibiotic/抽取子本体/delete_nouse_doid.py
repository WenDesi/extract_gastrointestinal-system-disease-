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


def write_file(filepath,llist):
    file_object = open(filepath,'w')

    for ele in llist:
        file_object.write(ele+'\n')
    file_object.close()

if __name__ == '__main__':

    ontology = read_ontology(full_ontology_filepath)

    pattern= re.compile(r'(?<=<oboInOwl:id rdf:datatype="http://www.w3.org/2001/XMLSchema#string">DOID:)\d+')
    ids = pattern.findall(ontology)
    print len(ids)

    pattern= re.compile(r'(?<=<rdfs:subClassOf rdf:resource="http://purl.obolibrary.org/obo/DOID_)\d+')
    sub = pattern.findall(ontology)
    print len(sub)

    results = set(sub) - set(ids)
    print len(results)
    for ele in results:
        print ele













