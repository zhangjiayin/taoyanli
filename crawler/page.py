# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
import re
from urlparse import urlparse
class TylCrawlerPage:

    def __init__(self, *args, **kwargs):
        self.referer=""
        self.url=""
        self.content=""
        self.level=1
        self.headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:11.0) Gecko/20100101 Firefox/11.0"}
        self.links = []
        self.code  = "0"
        self.responseHeaders = {}
        self.fetched = False
        self.cookieJar  = None
        self.fetcher = None
        for k in kwargs: setattr(self, k,kwargs[k])

    def setHeaders(self, **kwargs):
        for x in kwargs: setattr(self.headers, kwargs[k])

    def setReferer(self,referer):
        self.headers["Referer"] = referer

    def getLinks(self, host=""):
        self.parseLinks(host)
        return self.links

    def parseLinks(self, host):
        if self.links == [] and self.content != "":
            o =  urlparse(self.url)
            path = o.path.split('/');
            path.pop()
            absUrl = o.scheme + "://" + o.netloc + "/";
            relUrl = absUrl[0:-1]+("/".join(path)) + "/"
            urls = re.findall(r'href=[\'"]?([^\'" >]+)', self.content, re.IGNORECASE|re.MULTILINE)
            fixedUrl = [ self.fixUrl(x,absUrl, relUrl) for x in urls]
            fixedUrl = [ x for x in fixedUrl if self.filterHost(x, host) ]
            #for x in urls:
            #    fixedUrl
            self.links = fixedUrl
    def filterHost(self, url, host):
        o =  urlparse(url)
        if o.netloc.find(host) == -1:
            return False
        return True

    def fixUrl(self, url, absUrl, relUrl):
        if url[0:7] == "http://"  or url[0:8] == "https://" :
            return url
        if url[0:1] == '/':
            return absUrl[0:-1] + url
        return relUrl + url
