from urllib2 import urlopen
from HTMLParser import HTMLParser
from urlparse import urljoin
import re

def clean(url):
    if url[0:4] != "http":
        url = "http://" + url
    idx = url.find('#')
    if idx != -1:
        url = url[:idx]
    l = len(url)
    if url[l - 1] == '/':
        url = url[:l - 1]
    return url


def valid(url):
    '''
    Check if the given url is valid
    '''
    if re.match( r'^https?://(.*\.)?gocardless.com.*$', url, re.M|re.I ):
        return True
    else:
        return False


class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, val in attrs:
                if key == "href":
                    url = urljoin(self.url, val)
                    url = clean(url)
                    if valid(url):
                        self.urls.append(url)


    def run(self, url):
        self.url = url
        self.urls = []
        try:
            response = urlopen(url)
            html = response.read().decode("utf-8")
            self.feed(html)
        except:
            pass
        return self.urls


class Spider(object):
    def __init__(self):
        self.to_visit = []
        self.visted = set([])
        self.parser = HTMLParser()

    def walk(self, url):
        url = clean(url)
        self.to_visit.append(url)
        while len(self.to_visit) > 0:
            url = self.to_visit.pop(0)
            self.visted.add(url)
            print "Visiting:", url
            urls = self.parser.run(url)
            for url in urls:
                if url not in self.visted and url not in self.to_visit:
                    self.to_visit.append(url)


if __name__ == "__main__":
    spider = Spider()
    spider.walk("http://gocardless.com/")
