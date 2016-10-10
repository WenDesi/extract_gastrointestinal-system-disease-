# -*- coding: utf-8 -*-

import csv
import codecs

ontology_filepath = 'ontology/diseaseName.txt'
cdd39_filepath = 'ontology/rdf.csv'

def get_id_name(line):
    id = line[0]
    name = [line[1]]
    try:
        alias = line[2]
        alias_list = alias.split(',')
        name.extend(alias_list)
    except:
        pass

    return id,name

def read_csv(filepath):
    result = []

    reader = csv.reader(file(filepath, 'rb'))
    for line in reader:
        id,names = get_id_name(line)
        result.append((int(id),names))

    return result

def read_txt(filepath):
    result = []

    file_obj = codecs.open(filepath,'r','utf-8')
    while True:
        line = file_obj.readline()
        line=line.strip('\r\n')
        if not line:
            break
        result.append(line)
    file_obj.close()

    return result

def is_same(word1,word2):
    return word1 == word2

def get_same_items(ontology,cdd39):
    count = 0

    for disease1 in ontology:

        for item in cdd39:
            flag = False

            id = item[0]
            disease2 = item[1]

            for alias in disease2:
                if is_same(disease1,alias):
                    flag = True
                    break

            if flag:
                count += 1
                print count
                print '<%s> is same to <%s> which id is %d' % (disease1,disease2[0],id)

                break

if __name__ == '__main__':
    ontology = read_txt(ontology_filepath)
    cdd39 = read_csv(cdd39_filepath)

    get_same_items(ontology,cdd39)



