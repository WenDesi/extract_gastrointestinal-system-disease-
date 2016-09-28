# -*- coding: utf-8 -*-
import rdflib
import re
import Logger
OWL = u'E://实验室/知识图谱/暑假/疾病本体/解析肠道本体/ontology/doid.owl'
XML_PATH = u"http://www.w3.org/2001/XMLSchema"
# OWL = u"http://www.w3.org/2002/07/owl"

class owl_parse():
    """parser owl file """
    def __init__(self,path,logger):
        self.class_list = []   #save class in owl file
        self.domains = []  #save domains in owl file
        self.dict_class = {}
        self.dict_domain = {}
        self.namespace_re = re.compile(path)
        self.logger = logger
        re_line = "%s/" %path
        self.namespace_re_2 = re.compile(re_line)
        self.predict_dict = {}
        self.namespace_re_1 = re.compile(XML_PATH)
        self.namespace_re_3 = re.compile(OWL)
        self.type_relation = []
        self.general_list = []
        self.master_property = []

    def parser_line(self,line):
        if line and len(line):
            items = line.split('#')
            if len(items) == 2:
                namespace = items[0]
                value = items[1]
                return(namespace,value)
        return 0

    def parser_predict(self,object_value,object_path,predict_value,subject_value,subject_path):
        """property"""
        subject = "/%s/%s" %(subject_path,subject_value)
        object =   "/%s/%s" %(object_path,object_value)
        if  predict_value == 'type':
            if (object_value == "FunctionalProperty") or (object_value == "InverseFunctionalProperty"):
                if self.predict_dict.has_key(subject):
                    self.predict_dict[subject]['functional'] = True
                else:
                    dict_property = {}
                    dict_property['functional'] = 'true'
                    dict_property['name'] = subject_value
                    self.predict_dict[subject] = dict_property
            if (self.dict_class.has_key(object)): #individual define
                self.general_list.append((subject_value,object))
        if predict_value == 'domain':
            if self.predict_dict.has_key(subject):
                self.predict_dict[subject]['schema'] = object
            else:
                dict_property = {}
                dict_property['schema'] = object
                dict_property['name'] = subject_value
                self.predict_dict[subject] = dict_property

        if predict_value == 'range':
            if self.predict_dict.has_key(subject):
                if len(object_path) == 0:
                    self.predict_dict[subject]['datatype'] = object_value
                else:
                    self.predict_dict[subject]['datatype'] = object
            else:
                dict_property = {}
                if len(object_path) == 0:
                    dict_property['datatype'] = object_value
                else:
                    dict_property['datatype'] = object
                dict_property['name'] = subject_value
                self.predict_dict[subject] = dict_property
        if predict_value == 'inverseOf':
            self.master_property.append( (subject,object))

        if predict_value == 'subClassOf':
            self.type_relation.append((subject,object))
            if self.dict_class.has_key(object):
                pass
            else:
               domain = "/%s" %(object_path)
               self.class_list.append((domain,object_value))
        return 1

    def update_namespace(self,namespace):
        """all the namespace in owl file"""
        if len(namespace) == 0:
            return
        if re.findall(r'.owl',namespace):
            return
        if self.dict_domain.has_key(namespace):
            pass
        else:
            self.dict_domain[namespace] = 1
            self.domains.append(namespace)
    def get_master_property(self):
        res = []
        for item in self.master_property:
            value = item[1]
            key = item[0]
            if self.predict_dict.has_key(value) and self.predict_dict.has_key(key):
                dict1 = self.predict_dict[value]
                master_property_value = "%s/%s" %(dict1['schema'],dict1['name'])
                dict2 = self.predict_dict[key]
                master_property_key = "%s/%s" %(dict2['schema'],dict2['name'])
                res.append((master_property_key,master_property_value))
        return res

    def get_type_relation(self):
        """return class list(subject,object) """
        return self.type_relation

    def get_general_list(self):
       """individual in owl file"""
       return self.general_list

    def get_class(self):
        """return class list(domain,name) """
        list = []
        for item in self.class_list:
            namespace = item[0][1:]
            if self.dict_domain.has_key(namespace):
                list.append(item)
        return list

    def get_property(self):
        """ return property list"""
        keys = self.predict_dict.keys()
        property_list = []
        for key in keys:
            data_dict = self.predict_dict[key]
            property_list.append(data_dict)
        return property_list

    def get_domain(self):
        """return domain list"""
        return self.domains

    def parser_n3(self,s,p,o):
        """build class and finish parser"""
        ret = self.parser_line(o)
        if not ret:
            return -1
        object_value = ret[1]
        object_namespace = self.namespace_re_2.sub('',ret[0])
        object_namespace = self.namespace_re_1.sub('', object_namespace)
        object_namespace = self.namespace_re_3.sub('',object_namespace)

        ret = self.parser_line(p)
        if not ret:
            return -1
        predict_namespace = ret[0]
        predict_value = ret[1]

        ret = self.parser_line(s)
        if not ret:
            return -1
        subject_value = ret[1]
        subject_namespace_1 = self.namespace_re.sub('',ret[0])   #/domain
        subject_namespace = self.namespace_re_2.sub('',ret[0])   #domain
        subject_namespace = self.namespace_re_1.sub('',subject_namespace)
        subject_namespace = self.namespace_re_3.sub('',subject_namespace)

        self.update_namespace(subject_namespace)
        self.update_namespace(object_namespace)
        if(object_value == 'Class'):
            value = "%s/%s" %(subject_namespace_1,subject_value)
            self.dict_class[value] = 1
            self.class_list.append((subject_namespace_1,subject_value))
        else:
            self.parser_predict(object_value,object_namespace,predict_value,subject_value,subject_namespace)
        return 0
