import urllib2
import cookielib

class TylFetcher:
    def fetch(self,page):
        page.fetched = True
        if not hasattr(page, "url"):
            return None
        try:
            req = urllib2.Request(page.url)
            for x in page.headers: req.add_header(x, page.headers[x])
            if page.cookieJar is None:
                page.cookeJar = cookielib.CookieJar()
    
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(page.cookeJar))
            r = opener.open(req)
            response = r.read()
            page.code = r.getcode()
            page.content = response
            for header in r.info().headers:
                pair = header.split(":")
                headerKey = pair[0].strip()
                headerValue = pair[1].strip()
                page.responseHeaders[headerKey] = headerValue

        except Exception,e:
            print e

if __name__ == "__main__":
    from page import TylCrawlerPage
    fetcher = TylFetcher()
    page = TylCrawlerPage(url="http://www.taobao.com")
    fetcher.fetch(page)
    #print page.getLinks()
