#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv
import codecs

from add_entity import *
from add_relationship import *
from file_operation import *


def build_relation_dict(relation_pairs):
    '''
    :param relation_pairs:
    :return: dict[doid] = cs
    '''
    translator_filepath = 'translator.csv'
    translator = read_csv(translator_filepath)

    translator_dict = {}

    for line in translator:
        result = int(line[0])
        doid = line[2]
        sy_word = line[3]

        if result == 0:
            continue

        translator_dict[sy_word] = doid

    results = {}

    for relation_pair in relation_pairs:
        if len(relation_pair) != 2:
            continue

        disease = relation_pair[0]
        entity = relation_pair[1]

        if disease not in translator_dict:
            continue

        doid = translator_dict[disease]

        if doid not in results:
            results[doid] = [entity]
        else:
            results[doid].append(entity)

    return results


if __name__ == '__main__':
    # 需要改
    full_ontology_filepath = u'step3.owl'
    new_ontology_filepath = u'step3_ok.owl'
    ontology = read_ontology(full_ontology_filepath)

    # 需要改
    entity_filepath = 'bacteria.csv'
    entity = map(lambda x:x[0], read_csv(entity_filepath))

    # 需要改
    relation_filepath = 'disease_bacteria_relation.csv'
    relation = build_relation_dict(read_csv(relation_filepath))

    ontology = add_entity(ontology,entity)
    ontology = add_relationship(ontology,relation,entity)

    write_ontology(new_ontology_filepath,ontology)