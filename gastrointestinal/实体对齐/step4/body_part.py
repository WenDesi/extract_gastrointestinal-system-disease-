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
        line=line.strip('\r\n')
        if 'wdswdswds' in line:
            break
        result.append(line)
    file_obj.close()
    return result

def write_ontology(filepath,lines):
    file_object = open(filepath,'w')
    for line in lines:
        file_object.write(line+'\n')
    file_object.close()

def write_csv(filepath,llist):
    writer = csv.writer(file(filepath, 'wb'))
    for line in llist:
        writer.writerow(line)

def add_department(ontology,department_dict):
    new_ontology = []
    flag = False

    department_line = '		<oboInOwl:part_of_body rdf:datatype="&xsd;string">%s</oboInOwl:part_of_body>'

    disease_aliases = None
    doid_pattern = re.compile(r'(?<=<oboInOwl:id rdf:datatype="&xsd;string">DOID:).+?(?=</oboInOwl:id>)')
    end_pattern = re.compile(r'</owl:Class>')


    for line in ontology:

        line_disease = doid_pattern.findall(line)
        line_end = end_pattern.findall(line)

        if r'    // Classes' in line:
            print 'haha'

        if len(line_disease) > 0:
            disease = line_disease[0]
            if disease in department_dict:
                flag =  True
                disease_departments = department_dict[disease]
            else:
                flag = False

        elif line_end and flag:
            for disease_department in disease_departments:
                new_ontology.append(department_line % disease_department)

        new_ontology.append(line)

    return new_ontology

def build_department_dict(lines):
    dict = {}

    for line in lines:
        department = line[1:]
        doid = line[0].decode()
        dict[doid] = department

    return dict


if __name__ == '__main__':
    full_ontology_filepath = u'zh_gastrointestinal_step3.owl'
    new_ontology_filepath = u'zh_gastrointestinal_step4.owl'

    department_filepath = 'part_of_body.csv'



    ontology = read_ontology(full_ontology_filepath)
    print 'end read'
    department_dict = build_department_dict(read_csv(department_filepath))

    print 'end read'

    new_ontology = add_department(ontology,department_dict)
    write_ontology(new_ontology_filepath,new_ontology)

















