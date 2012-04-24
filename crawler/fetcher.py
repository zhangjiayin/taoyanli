import urllib2

class TylFetcher:
    def fetch(self,page):
        page.fetched = True
        if not hasattr(page, "url"):
            return None
        try:
            req = urllib2.Request(page.url)
            for x in page.headers: req.add_header(x, page.headers[x])
            r = urllib2.urlopen(req)
            response = r.read()
            page.content = response
        except Exception,e:
            print e

if __name__ == "__main__":
    from page import TylCrawlerPage
    fetcher = TylFetcher()
    page = TylCrawlerPage(url="http://www.taobao.com")
    fetcher.fetch(page)
    print page.getLinks()
