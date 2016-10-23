#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree

full_ontology_filepath = u'E://实验室/知识图谱/暑假/疾病本体/解析肠道本体/ontology/doid.owl'



def get_subclass_of_parent(owl_Classes,root,parent_id):
    childrens = []

    for owl_Class in owl_Classes:

        url = owl_Class.attrib['{'+root.nsmap['rdf']+'}about']
        doid = url[url.index('_')+1:]

        sub_classes = owl_Class.findall('rdfs:subClassOf',root.nsmap)

        for sub_class in sub_classes:

            sub_url = sub_class.attrib['{'+root.nsmap['rdf']+'}resource']
            sub_doid = sub_url[sub_url.index('_')+1:]

            if sub_doid == parent_id:
                childrens.append(doid)

    return childrens

def write_file(filepath,llist):
    file_object = open(filepath,'w')

    for ele in llist:
        file_object.write(ele+'\r\n')
    file_object.close()

if __name__ == '__main__':

    tree = etree.parse(full_ontology_filepath)
    root = tree.getroot()

    owl_Classes = root.findall('owl:Class',root.nsmap)


    clawed_id = []
    unclaw_id = ['77']
    results = ['77']

    count = 0
    while len(unclaw_id) > 0:
        doid = unclaw_id[0]
        unclaw_id = unclaw_id[1:]

        if doid in clawed_id:
            continue

        sub_id = get_subclass_of_parent(owl_Classes,root,doid)

        print 'round %d :' % count,sub_id


        count += 1
        clawed_id.append(doid)
        results.extend(sub_id)
        unclaw_id.extend(sub_id)

    results = set(results)
    print len(results)
    print results


    id_filepaht = 'ids.txt'
    write_file(id_filepaht,results)






