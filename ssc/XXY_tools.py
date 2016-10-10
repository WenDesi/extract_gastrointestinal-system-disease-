# -*- coding: utf-8 -*-
import textDealer

import re
import csv
import codecs
import urllib2
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import time


#潇湘园的翻译
class XXY_translator(object):

    def post_DXY(self,url):
        print url
        try:
            timeout = 5
            request = urllib2.Request(url)
            #伪装HTTP请求
            request.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
            request.add_header('connection','keep-alive')
            request.add_header('referer', url)
            # request.add_header('Accept-Encoding', 'gzip')  # gzip可提高传输速率，但占用计算资源
            response = urllib2.urlopen(request, timeout = timeout)
            html = response.read()
            #if(response.headers.get('content-encoding', None) == 'gzip'):
            #    html = gzip.GzipFile(fileobj=StringIO.StringIO(html)).read()
            response.close()
            # print html
            return html
        except Exception as e:
            print 'URL Request Error:', e
            return None

    def get_alias_from_html(self,html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        # li = soup.find(id="radical")
        # radical = li.span.contents[0]
        res = set()
        print 'called'
        li = soup.find_all('h3')#(_class = "x_title3 m7")
        print li
        for i in li:
            temp =  unicode(i.string)#.encode('utf8')
            # print type(temp)
            if temp == None or temp == 'None':
                continue
            temp = temp.replace('\t','')
            temp = temp.replace('\n','')
            temp = temp.replace(' ','')
            print temp
            if ',' in temp:
                temp = temp.split(',')
                for ii in temp:
                    res.add(ii)
                continue
            res.add(temp)
        for i in res:
            print i,'|',
        print ''
        return res

    def anlysis_from_html(self,html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        li = soup.find_all('div',class_ = 'content')
        # res = set()
        res = []
        for i in li:
            if i.string == None:
                continue
            t = i.string.split(';')
            for j in t:
                res += j.lstrip(),
        # print res
        return res

        # wds = pq(html_doc)
        # llist = wds('.x_title3').children('a').children('b')
        # res = set()
        # for ele in llist:
        #     ssc = pq(ele)
        #     # print ssc.text()
        #     for i in ssc.text().split(','):
        #         res.add(i.lower())
        # for i in res:
        #     print i,'|',
        # print ''
        # return res

    def translateWord(self,word):
        res = None
        while True:
            print word
            html = self.post_DXY("http://www.mcd8.com/w/" +word)
            # print html
            if html == None:
                return None
            # elif "您的访问过于频繁，休息一会吧。" in html:
            #     print '!!!!'
            #     time.sleep(0)
            #     print '!!!!'
            else:
                # html = self.post_DXY("http://www.mcd8.com/w/" +word)
                res = self.anlysis_from_html(html)
                # print res
                break
            # res = self.anlysis_from_html(html)
        return res

    def getSymptoms(self,filepath):
        # filepath = '.\data\\try8.txt'
        file_obj = codecs.open(filepath,'r','utf-8')
        try:
            count = 0
            for i in file_obj:
                # print i
                count += 1
                if count < 50 or (count < 4767 and count > 317):
                    continue
                print count

                i = i.split('|')
                spt = i[2]
                # if spt == '@':
                #     pass
                spts = spt.split(';')
                db = DBconnector.DBconnector()
                for j in spts:
                    # print j
                    en = ''
                    res_set = self.translateWord(j.encode('utf8'))
                    print res_set
                    if res_set == None:
                        # db.insert(i[0],i[1],j,'')
                        continue
                    for iii in res_set:
                        en += iii + '|'
                    # print en
                    # db.insert(i[0],i[1],j,en)

        finally:
            file_obj.close()


    def getSymptomsFromCSV(self,filepath):
        # filepath = '.\data\\try8.txt'
        file_obj = codecs.open(filepath,'r','utf-8')
        #file_object = open("res.csv",'a')
        try:
            count = 0
            content = ''
            for i in file_obj:
                # print i
                count += 1
                # if count > 14:
                #     break
                print count

                # i = i.split(',')
                # spt = i[2]
                i = i[:-2]
                # print i
                spts = i.split(',')

                for j in spts:
                    # print j
                    en = ''
                    res_set = self.translateWord(j.encode('utf8'))
                    print res_set
                    if res_set == None:
                        # db.insert(i[0],i[1],j,'')
                        content += j + ',' + en + '\n'
                        continue
                    for iii in res_set:
                        en += iii + '|'
                    print j,en
                    content += j + ',' + en + '\n'
                    # file_object.write(content.encode('utf8'))
                    # content = ''
                    # db.insert(i[0],i[1],j,en)
            print content
            file_object = open("res.csv",'w')
            file_object.write(content.encode('utf8'))
            file_object.close()
            # writer = csv.writer(file('res.csv', 'wb'))
            #         # writer.writerow(['Column1', 'Column2', 'Column3'])
            #         # lines = [range(3) for i in range(5)]
            #         # for line in lines:
            # writer.write(content.encode('utf8'))
        finally:
            file_obj.close()

# trans.translateWord('感冒')

# wordList = ["卵巢肿瘤","卵巢囊肿","卵巢小囊肿","卵巢占","卵巢包块","子宫内膜息肉","子宫内膜增厚","宫腔占位","子宫内膜增生","子宫内膜占位","宫腔积液","子宫脱垂","子宫内膜厚","子宫内膜回声不均","宫腔积血","子宫内膜囊肿","子宫息肉","子宫平滑肌瘤","子宫内液性占位","子宫增大","子宫内膜病变","子宫内膜简单增生","子宫粘膜下肌瘤","子宫内膜回声占位","子宫脱出"]
# for i in wordList:
#     trans.translateWord(i)

# trans = DXY_translator()
# trans.getSymptoms()


# trans = XXY_translator()
# # trans.getSymptoms()
# trans.getSymptomsFromCSV('.\data\\merge.csv')
# # trans.translateWord('关节痛')