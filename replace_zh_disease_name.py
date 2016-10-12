#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import codecs

full_ontology_filepath = u'ontology/zh_gastrointestinal.owl'
disease_name_filepath = 'ontology/zh_diseaseName.csv'

def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rU'))
    for line in reader:
        results.append(line)
    return results

def read_ontology(filepath):
    results = []

    file_obj = codecs.open(filepath,'r','utf-8')
    while True:
        line = file_obj.readline()
        line=line.strip('\r\n')
        if 'wdswdshcyhcy' in line:
            break
        results.append(line)
    file_obj.close()
    return results

def replace_disase_name(ontology,zh_dict):
    results = []
    i = 0
    while i < len(ontology):
        line = ontology[i]

        if '<rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">' in line:
            left = line.index('>') + 1
            right = line.index(r'</')

            name = line[left:right]
            print line
            print name

            if name in zh_dict:
                zh_name = zh_dict[name]
                print zh_name.encode()
                line = line.replace(name,zh_name)

        results.append(line)

        i += 1
    return results


def write_file(filepath,llist):
    file_object = open(filepath,'w')

    for ele in llist:
        file_object.write(ele+'\n')
    file_object.close()

if __name__ == '__main__':

    ontology = read_ontology(full_ontology_filepath)
    zh_ = read_csv(disease_name_filepath)

    zh_dict = {}
    for line in zh_:
        zh_dict[line[1]] = line[0]

    ontology = replace_disase_name(ontology,zh_dict)
    write_file(full_ontology_filepath,ontology)








