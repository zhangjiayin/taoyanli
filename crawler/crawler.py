# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
from page import TylCrawlerPage

class TylCrawler:
    def __init__(self,host="",**kwargs):
        for k in kwargs: setattr(self, k,kwargs[k])
        pass
