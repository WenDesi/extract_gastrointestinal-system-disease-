#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

def contain_zh(word):
    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    word = word.decode()
    global zh_pattern
    match = zh_pattern.search(word)

    return match

if __name__ == '__main__':
    word1 = 'ceshi,测试'
    word2 = 'ceshi,ceshi'

    if contain_zh(word1):
        print '%s 里面有中文' % word1
    if contain_zh(word2):
        print '%s 里面有中文' % word2