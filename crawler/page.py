# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
import re

class TylCrawlerPage:

    def __init__(self, *args, **kwargs):
        self.referer=""
        self.url=""
        self.content=""
        self.level=1
        self.headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:11.0) Gecko/20100101 Firefox/11.0"}
        self.links = []
        self.fetched = False
        for k in kwargs: setattr(self, k,kwargs[k])

    def setHeaders(self, **kwargs):
        for x in kwargs: setattr(self.headers, kwargs[k])

    def setReferer(self,referer):
        self.headers["Referer"] = referer

    def getLinks(self):
        self.parseLinks()
        return self.links

    def parseLinks(self):
        if self.links == [] and self.content != "":
            urls = re.findall(r'href=[\'"]?([^\'" >]+)', self.content, re.IGNORECASE|re.MULTILINE)
            self.links = urls
