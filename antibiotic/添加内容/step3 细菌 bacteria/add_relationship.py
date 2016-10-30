#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from add_entity import *

def bian(word):
    if word[0].islower():
        return word.capitalize()
    else:
        return word[0].lower() + word[1:]


def add_relationship(ontology,dict,entity):
    new_ontology = []
    flag = False


    relationships = None
    disease_pattern = re.compile(r'(?<=<owl:Class rdf:about="&obo;DOID_).+?(?=">)')
    end_pattern = re.compile(r'</owl:Class>')


    for line in ontology:

        line_disease = disease_pattern.findall(line)
        line_end = end_pattern.findall(line)


        if len(line_disease) > 0:
            doid = line_disease[0]
            if doid in dict:
                flag =  True
                relationships = dict[doid]
            else:
                flag = False

        elif line_end and flag:
            # 需要改
            father = 'caused_by'

            for relation in relationships:
                if len(relation) < 1:
                    continue

                if relation not in entity:
                    bian_relation = bian(relation)
                    if bian_relation in entity:
                        relation = bian_relation

                line1 = '        <owl:equivalentClass>\n'
                line2 = '            <owl:Restriction>\n'
                line3 = '                <owl:onProperty rdf:resource="&obo;doid#%s"/>\n' % father
                line4 = '                <owl:someValuesFrom rdf:resource="&obo;doid.owl#%s"/>\n' % rebuild(relation)
                line5 = '            </owl:Restriction>\n'
                line6 = '        </owl:equivalentClass>\n'


                new_ontology.append(line1)
                new_ontology.append(line2)
                new_ontology.append(line3)
                new_ontology.append(line4)
                new_ontology.append(line5)
                new_ontology.append(line6)

        new_ontology.append(line)

    return new_ontology