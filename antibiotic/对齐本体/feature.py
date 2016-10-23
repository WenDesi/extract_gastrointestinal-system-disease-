#!/usr/bin/python
# -*- coding: utf-8 -*-



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