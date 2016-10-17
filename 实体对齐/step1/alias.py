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

def read_ontology(filepath):
    result = []
    file_obj = codecs.open(filepath,'r','utf-8')
    while True:
        line = file_obj.readline()
        # line=line.strip('\r\n')
        if 'wdswdswds' in line:
            break
        result.append(line)
    file_obj.close()
    return result

def write_ontology(filepath,lines):
    file_object = open(filepath,'w')
    for line in lines:
        file_object.write(line)
    file_object.close()

def write_csv(filepath,llist):
    writer = csv.writer(file(filepath, 'wb'))
    for line in llist:
        writer.writerow(line)

def add_alias(ontology,alias_dict):
    new_ontology = []
    flag = False

    alias_line = '        <oboInOwl:hasExactSynonym rdf:datatype="&xsd;string">%s</oboInOwl:hasExactSynonym>\n'

    disease_aliases = None
    disease_pattern = re.compile(r'(?<=<rdfs:label rdf:datatype="&xsd;string">).+?(?=</rdfs:label>)')
    end_pattern = re.compile(r'</owl:Class>')


    for line in ontology:

        line_disease = disease_pattern.findall(line)
        line_end = end_pattern.findall(line)

        if r'    // Classes' in line:
            print 'haha'

        if len(line_disease) > 0:
            disease = line_disease[0]
            if disease in alias_dict:
                flag =  True
                disease_aliases = alias_dict[disease]

        elif line_end and flag:
            for alias in disease_aliases:
                new_ontology.append(alias_line % alias)

        new_ontology.append(line)

    return new_ontology

def build_alias_dict(lines):
    dict = {}

    for line in lines:
        aliases = line[1:]
        name = line[0].decode()
        dict[name] = aliases

    return dict


if __name__ == '__main__':
    full_ontology_filepath = u'zh_gastrointestinal_delete_nouse_subclass_test.owl'
    new_ontology_filepath = u'zh_gastrointestinal_step1.owl'

    diseaseName_filepath = 'zh_diseaseName.csv'



    ontology = read_ontology(full_ontology_filepath)
    print 'end read'
    alias_dict = build_alias_dict(read_csv(diseaseName_filepath))

    print 'end read'

    new_ontology = add_alias(ontology,alias_dict)
    write_ontology(new_ontology_filepath,new_ontology)

















