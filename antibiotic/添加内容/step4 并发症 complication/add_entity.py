#!/usr/bin/python
# -*- coding: utf-8 -*-

def rebuild(line):
    new_line = line.replace(' ','_')
    new_line = new_line.replace('&','&amp;')
    new_line = new_line.replace('>','&gt;')
    new_line = new_line.replace('<','&lt;')
    new_line = new_line.replace('\'','&apos;')
    new_line = new_line.replace('\"','&quot;')

    return new_line


def get_insert_index(ontology):
    for i, line in enumerate(ontology):
        if '<!-- insert entity here -->' in line:
            return i+2


def add_entity(ontology,entitys):
    insert_index = get_insert_index(ontology)

    # 需要改
    father = 'complication'

    line1 = '    <owl:Class rdf:about="&obo;doid.owl#%s"/>\n' % father
    line2 = '\n'
    line3 = '    <!-- http://purl.obolibrary.org/obo/doid.owl#%s -->\n' % father

    ontology.insert(insert_index,line1)
    ontology.insert(insert_index,line2)
    ontology.insert(insert_index,line3)
    ontology.insert(insert_index,line2)


    line4 = '    </owl:Class>\n'
    line5 = '        <rdfs:subClassOf rdf:resource="&obo;doid.owl#%s"/>\n' % father
    line6 = '        <rdfs:label rdf:datatype="&xsd;string">%s</rdfs:label>\n'
    line7 = '    <owl:Class rdf:about="&obo;doid.owl#%s">\n'
    line8 = '    <!-- http://purl.obolibrary.org/obo/doid.owl#%s -->\n'

    for entity in entitys:
        line6_new = line6 % entity
        line7_new = line7 % rebuild(entity)
        line8_new = line8 % rebuild(entity)

        ontology.insert(insert_index,line2)
        ontology.insert(insert_index,line4)
        ontology.insert(insert_index,line5)
        ontology.insert(insert_index,line6_new)
        ontology.insert(insert_index,line7_new)
        ontology.insert(insert_index,line8_new)
        ontology.insert(insert_index,line2)

    return ontology

