# -*- coding: utf-8 -*-

import csv
import codecs

from ssc.XXY_tools import *
import ssc.XXY_tools

ontology_filepath = 'ontology/diseaseName.txt'

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

def get_translate(ontology):
    trans = XXY_translator()

    for disease in ontology:
        disease = disease.replace(' ','-')

        translate = trans.translateWord(disease)

        if translate:
            translate = ' |'.join(translate)
            print '<%s> 翻译为 <%s>' % (disease,translate)

if __name__ == '__main__':
    ontology = read_txt(ontology_filepath)

    get_translate(ontology)