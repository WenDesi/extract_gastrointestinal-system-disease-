#!/usr/bin/python
# -*- coding: utf-8 -*-

from xpinyin import Pinyin
import chardet

def calPinyinEditDistance(word1,word2):
    p = Pinyin()
    word1_pinyin = p.get_pinyin(word1.decode())
    word2_pinyin = p.get_pinyin(word2.decode())

    word1_pinyin = word1_pinyin.replace('-','')
    word2_pinyin = word2_pinyin.replace('-','')

    return calEditDistance(word1_pinyin,word2_pinyin)

def calEditDistance(m,n):
    """compute the least steps number to convert m to n by insert , delete , replace .
    动态规划算法,计算单词距离
    print word_distance("abc","abec")
    1
    print word_distance("ababec","abc")
    3
    """

    #print m,n,len(m),chardet.detect(m)
    len_1=lambda x:len(x)+1
    c=[[i] for i in range(0,len_1(m)) ]
    c[0]=[j for j in range(0,len_1(n))]

    for i in range(0,len(m)):
    #    print i,' ',
        for j in range(0,len(n)):
            c[i+1].append(
                min(
                    c[i][j+1]+1,#插入n[j]
                    c[i+1][j]+1,#删除m[j]
                    c[i][j] + (0 if m[i]==n[j] else 1 )#改
                )
            )
    #        print c[i+1][j+1],m[i],n[j],' ',
    #    print ''
    edit_distance = c[-1][-1]
    edit_distance_score = 1.0 - (edit_distance+0.0) / max(len(m),len(n))
    return edit_distance_score# c[-1][-1]