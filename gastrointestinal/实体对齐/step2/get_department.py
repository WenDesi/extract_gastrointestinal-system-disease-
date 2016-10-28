#!/usr/bin/python
# -*- coding: utf-8 -*-


import csv

from SQLConnector import *

def read_csv(filepath):
    results = []
    reader = csv.reader(file(filepath, 'rU'))
    for line in reader:
        results.append(line)
    return results

def write_csv(filepath,llist):
    writer = csv.writer(file(filepath, 'wb'))
    for line in llist:
        writer.writerow(line)

def get_department(sqlConn,id):
    sql = 'select department from neike where id = %s;' % id
    result = sqlConn.select(sql)

    return result[0][0]


if __name__ == '__main__':
    doid_filepath = 'same_entity_with_doid.csv'
    department_filepath = 'department.csv'

    doid_lines = read_csv(doid_filepath)

    result = []
    sql_conn = SqlConnector(db='disease_ontology')
    for line in doid_lines:
        doid = line[0]
        department = get_department(sql_conn,line[1])

        result.append([doid,department])

    write_csv(department_filepath,result)
