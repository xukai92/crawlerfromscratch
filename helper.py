# This file contains helper functions for the web crawler.
# Author: Kai Xu
# Date: 06/11/2016


from urlparse import urlparse   # for domain extraction
import re                       # for regular expression


def clean(url):
    '''
    Clean up url by
        - remove "http://" or "https://"
        - remove element jumping
        - remove last '/'
    @input:
        url     :   the url to be processed
    @output:
        url     :   the clean url
    '''
    # Deal with "http(s)://"
    if url[0:7] == "http://":
        url = url[7:]
    if url[0:8] == "hppts://":
        url = url[8:]

    # Deal with "#"
    idx = url.find('#')
    if idx != -1:
        url = url[:idx]

    # Deal with last "/"
    l = len(url)
    if url[l - 1] == '/':
        url = url[:l - 1]

    return url


def get_domain(url):
    '''
    Get the domain of a given url
    @input:
        url     :   the url to be processed
    @output:
        domain  :   the domain of the url
    '''
    parsed_url = urlparse(url)
    return "{url.netloc}".format(url=parsed_url)


def valid(url, domain):
    '''
    Check if the given url is valid (e.g. within in "gocardless.com" domain)
    @input:
        url     :   the url to be checked
    @output:
        valid?  :   if the url is valid
    '''
    if re.match(r'^https?://([\w-]*\.)?' + domain + r'.*$', url, re.M|re.I):
        return True
    else:
        return False


def contain_static(val):
    '''
    Check if a given val (relative path or url) contains static files
    @input:
        val         :   relative path or url
    @output:
        contain?    :   if the val contains a static file
    '''
    if re.match(r'^.*\.(jpg|jpeg|gif|png|css|js|ico|xml|rss|txt).*$', val, re.M|re.I):
        return True
    else:
        return False


if __name__ == "__main__":
    print "I don't like snakes. Don't python me directly."
