# -*- coding: utf-8 -*-

import json
import urllib2
import cookielib

from pyquery import PyQuery as pq

class YMT(object):

    def __init__(self):
        """
        读取从 EditThisCookie 上获取的cookie
        并将其绑定到 urllib2 上
        以后每次爬虫访问网站时都会自动带上cookie，不再需要人工参与
        """

        cookie_jar = cookielib.MozillaCookieJar()
        cookies = open('cookie.txt').read()
        for cookie in json.loads(cookies):
            cookie_jar.set_cookie(cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False, domain=cookie['domain'], domain_specified=False, domain_initial_dot=False, path=cookie['path'], path_specified=True, secure=cookie['secure'], expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar),urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def _get(self, url):
        """
        :param url: 需要访问的url
        :return:    返回该url的网页内容
        """

        request = urllib2.Request(url=url)
        request.add_header('Referer', 'http://meddic.medlive.cn/search/search.do')
        response = urllib2.urlopen(request)
        data = response.read()

        return data

    def dict1(self,html):
        # 用 pyquery 定位翻译
        q = pq(html)
        paraphrase_list = q('.paraphrase_list')

        for paraphrase in paraphrase_list:
            p = pq(paraphrase)

            if p('.dictionary').text() == '英汉医学短语词典':
                return p('.dictionary_message').text()

        return None

    def dict2(self,html):
        # 用 pyquery 定位翻译
        q = pq(html)
        paraphrase_list = q('.paraphrase_list')

        for paraphrase in paraphrase_list:
            p = pq(paraphrase)

            if p('.dictionary').text() == '英文Sonmed词典':
                return p('.dictionary_message').text()

        return None

    def dict3(self,html):
        if '的相关词典解释' in html:
            return False
        return True

    def get_word_translate(self,word):
        """
        :param word: 需要翻译的英文单词
        :return: 如果有对应英文的中文，则返回该中文翻译，否则返回None
        """

        url = 'http://meddic.medlive.cn/search/search.do?word=%s' % word.replace(' ','+')
        html = self._get(url)

        if '您的访问过于频繁' in html:
            return -1

        return self.dict3(html)


if __name__ == '__main__':
    ymt = YMT()
    word = 'esophageal diverticulosis'
    print ymt.get_word_translate(word)


