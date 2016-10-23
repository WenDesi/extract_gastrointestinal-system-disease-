#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs

full_ontology_filepath = u'ontology/doid.owl'
new_ontology_filepath = u'ontology/gastrointestinal.owl'
gas_id_filepath = 'ids.txt'

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
            break
        results.append(line)
    file_obj.close()
    return results

def extract_gastrointestinal(ontology,ids):
    results = []
    i = 0
    old = '-1'

    while i < len(ontology):

        line = ontology[i]

        if '<!-- http://purl.obolibrary.org/obo/DOID_' in line:
            left = line.index('_') + 1
            right = line.index(' -->')

            id = line[left:right]
            if id == old:
                i += 1
                continue
            old = id

            if id not in ids:
                i += 1
                print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
                while '<!-- http://purl.obolibrary.org/obo/DOID_' not in ontology[i]:

                    print i
                    i += 1
                continue
            else:
                results.append(line)

        else:
            results.append(line)

        i += 1
    return results



def write_file(filepath,llist):
    file_object = open(filepath,'wb')


    for ele in llist:
        print ele
        file_object.write(ele.encode()+'\n')

    file_object.close()

if __name__ == '__main__':

    ids = read_file(gas_id_filepath)
    ontology = read_ontology(full_ontology_filepath)


    new_ontology = extract_gastrointestinal(ontology,ids)
    write_file(new_ontology_filepath,new_ontology)








