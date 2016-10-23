# -*- coding: utf-8 -*-  
import sys
# from PyQt4 import QtGui,QtCore
import urllib
import json
import chardet
from urllib import urlencode
import re
# import translator

def getFileContent(filename):

    f = open('.\data\\' + filename,"r")
    return f

def printList(list):
    print json.dumps(list,encoding='utf-8',ensure_ascii=False)


def getDiseases():

    symptoms_list = []
    # C:\Users\PrlNcE\Desktop\Translator\data\symptom_wds.txt
    symptoms_data = getFileContent("disease_name.txt")

    for line in symptoms_data:
        line.strip()
        symptoms_list.append(line[:-1])

    # print 'all symptoms:',
    # for i in symptoms_list:
    #     print i,
    # print ''
    return symptoms_list
    #print symptoms_list

def getSymptoms():

    symptoms_list = []
    # C:\Users\PrlNcE\Desktop\Translator\data\symptom_wds.txt
    symptoms_data = getFileContent("symptom_wds.txt")

    for line in symptoms_data:
        line.strip()
        symptoms_list.append(line[:-1])

    # print 'all symptoms:',
    # for i in symptoms_list:
    #     print i,
    # print ''
    return symptoms_list
    #print symptoms_list


def getAlias():
    symptoms_data = getFileContent('disease_alias_wds.txt')
    alias_list = []
    alias_dic = {}

    for line in symptoms_data:
        # line.decode('gb2312')
        # print chardet.detect(line)
        line.strip()
        alias_list.append(line[:-1])

    for i in alias_list[:]:
        try:
            i = i.decode('gb2312').encode('utf8')
            temp = i.split('|')

            key = temp[0][1:]
            # printList(temp)
            values = temp[1].split(';')
            for v in values:
                if re.match('^[A-Za-z \'－-]+$',v):
                    continue
                alias_dic[key] = alias_dic.get(key,[]) + [v]

            # printList(alias_dic.items())

        except:
            # print '~~'
            continue


    return alias_dic
    # print len(alias_list)

def writeAliasToFile(filename):
    alias_dic = getAlias()

    print len(alias_dic)

    f = open(filename, 'w')
    f.close()
    for k,v in alias_dic.items():
        f = open(filename, 'a')

        # print chardet.detect(k)
        f.write(k + ' ')
        for i in v:
            # print(i)
            f.write(i + ' ')
        f.write('\n')
        f.close()


# writeAliasToFile('C:\Users\PrlNcE\Desktop\Word2Vec\synonym\\alias_wds.txt')
# printList(alias_dic.keys())