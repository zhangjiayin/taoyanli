# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
#4 deep copy cookieJar import copy and  copy.deepcopy()
from page import TylCrawlerPage
from fetcher import TylCrawlerFetcher
from urlparse import urlparse

class TylCrawler:
    def __init__(self,host="",**kwargs):
        self.host = host
        for k in kwargs: setattr(self, k,kwargs[k])
        self.crawledList = []

    def crawl(self, url,fun, deep=5):
        page = TylCrawlerPage(url=url)
        fetcher = TylCrawlerFetcher()
        pages = [] 
        pages.append([page])

        try:
            for i in range(deep):
                pn = []
                for p in pages[i]:
                    fetcher.fetch(p)
                    links = p.getLinks(self.host)
                    fun(p)
                    if (i+1) == deep:
                        continue
                    for link in links:
                        try:
                            if self.crawledList.index(link) != -1:
                                continue
                        except ValueError as e:
                            pass
                        self.crawledList.append(link)
                        pchild = TylCrawlerPage(url=link)
                        pchild.setReferer(p.url)
                        pchild.cookieJar = p.cookieJar
                        pchild.level = i+1
                        pn.append(pchild)
                        #print link
                pages.append(pn)
        except ValueError as e:
            print e

if __name__ == "__main__":
    def p(v):
        print v.__class__.__name__
        #print v.content
        print v.code
        print v.cookieJar
        print v.responseHeaders

    crawler = TylCrawler('google.com')
    crawler.crawl('http://www.google.com',p,1)

