from urllib2 import urlopen
from HTMLParser import HTMLParser
from urlparse import urljoin
import re


def clean(url):
    '''
    Clean up url by
        - always start with "http://" or "https://"
        - remove element jumping
        - remove last '/'
    @input:
        url     :   the url to be processed
    @output:
        url     :   the clean url
    '''
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
    @input:
        url     :   the url to be checked
    @output:
        ???     :   if the url is valid
    '''
    if re.match( r'^https?://([\w-]*\.)?gocardless.com.*$', url, re.M|re.I ):
        return True
    else:
        return False


class HTMLParser(HTMLParser):
    '''
    HTML parser to fetch urls and show assests
    '''

    def handle_starttag(self, tag, attrs):
        '''
        Overrid of the default function to handle <a> and ??? tags
        TODO: update this comments when assest handle is done
        '''
        if tag == "a":
            for key, val in attrs:
                if key == "href":
                    url = urljoin(self.url, val)    # append relative path to the root path
                    url = clean(url)                # clean up url
                    if valid(url):
                        self.urls.append(url)       # append url to the return list
        # TODO: handle assesst

    def run(self, url):
        '''
        Run the parser and return links in this page
        '''
        self.url = url  # save root path
        self.urls = []  # init return list

        # Open the url and parse it
        # FIXME: 
        # There will be potential error when some website handshake is unsuccessful due to the SSL.
        # This is temporarly fixed by ignoring such failure but it should be further investiagted.
        try:
            response = urlopen(url)
            html = response.read().decode("utf-8")
            self.feed(html)
        except KeyboardInterrupt:
            exit()
        except:
            pass

        return self.urls


class Spider(object):
    def __init__(self):
        self.to_visit = []
        self.visted = set([])
        self.parser = HTMLParser()

    def crawl(self, target_url):
        target_url = clean(target_url)
        self.to_visit.append(target_url)

        while len(self.to_visit) > 0:
            url = self.to_visit.pop(0)
            self.visted.add(url)
            print "The spider is visiting:", url
            urls = self.parser.run(url)
            for url in urls:
                if url not in self.visted and url not in self.to_visit:
                    self.to_visit.append(url)

        print "The spider has finished crawling the web at {url}".format(url=target_url)

if __name__ == "__main__":
    spider = Spider()
    spider.crawl("http://gocardless.com/")
