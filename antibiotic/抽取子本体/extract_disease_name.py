#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs

full_ontology_filepath = u'ontology/antibiotic.owl'
disease_name_filepath = 'ontology/diseaseName.txt'

def read_file(filepath):
    results = []

    file_obj = codecs.open(filepath,'r','utf-8')
    while True:
        line = file_obj.readline()
        line=line.strip('\r\n')
        if not line:
            break
        results.append(line)
    file_obj.close()
    return results

def read_ontology(filepath):
    results = []

    file_obj = codecs.open(filepath,'r','utf-8')
    while True:
        line = file_obj.readline()
        line=line.strip('\r\n')
        if 'wdswdshcyhcy' in line:
            results.append(line)
            break
        results.append(line)
    file_obj.close()
    return results

def extract_name(ontology):
    results = []
    i = 0
    while i < len(ontology):
        line = ontology[i]

        if '<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
            left = line.index('>') + 1
            right = line.index(r'</')

            name = line[left:right]
            results.append(name)

        i += 1
    return results



def write_file(filepath,llist):
    file_object = open(filepath,'w')

    for ele in llist:
        file_object.write(ele+'\n')
    file_object.close()

if __name__ == '__main__':

    ontology = read_ontology(full_ontology_filepath)


    names = extract_name(ontology)
    write_file(disease_name_filepath,names)








