#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree

full_ontology_filepath = u'E://实验室/知识图谱/暑假/疾病本体/解析肠道本体/ontology/doid.owl'


tree = etree.parse(full_ontology_filepath)
root = tree.getroot()

print root.nsmap

owl_Classes = root.findall('owl:Class',root.nsmap)


for owl_Class in owl_Classes:

    url = owl_Class.attrib['{'+root.nsmap['rdf']+'}about']
    doid = url[url.index('_')+1:]

    if doid == '77':
        print type(owl_Class)
        print owl_Class.values

        # sub_classes = owl_Class.findall('rdfs:subClassOf',root.nsmap)

        # for sub_class in sub_classes:
        #     print sub_class.attrib
        #     print '{'+root.nsmap['rdf']+'}resource'
        #     sub_url = sub_class.attrib['{'+root.nsmap['rdf']+'}resource']
        #     print sub_url





